from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os


from db import get_db
from forms import LoginForm, RegisterForm
from models import get_user_by_username, get_user_by_id
from mysql.connector import Error
from init_db import init_database

load_dotenv()
init_database()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['WTF_CSRF_TIME_LIMIT'] = None

csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return User(user["id"], user["username"], user["password"])
    return None


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = get_user_by_username(form.username.data)

        if user and check_password_hash(user["password"], form.password.data):
            login_user(User(user["id"], user["username"], user["password"]))
            return redirect(url_for("dashboard"))
        else:
            form.username.errors = ["Usuario o contraseña incorrectos"]

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    form = RegisterForm()

    if form.validate_on_submit():
        db = None
        cursor = None
        
        try:
            user_exists = get_user_by_username(form.username.data)
            if user_exists:
                form.username.errors = ["Este usuario ya existe"]
                return render_template("register.html", form=form)
            
            db = get_db()
            cursor = db.cursor()

            hashed = generate_password_hash(form.password.data)

            cursor.execute(
                "INSERT INTO usuarios (username, password) VALUES (%s, %s)",
                (form.username.data, hashed)
            )

            db.commit()
            return redirect(url_for("login"))
        
        except Error as e:
            if db:
                db.rollback()
            print(f"Error en registro: {e}")
            form.username.errors = ["Error al registrar usuario"]
        
        finally:
            if cursor:
                cursor.close()
            if db:
                db.close()

    return render_template("register.html", form=form)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)