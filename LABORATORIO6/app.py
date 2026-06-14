from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave_segura"

csrf = CSRFProtect(app)

nombre_usuario = "Usuario"

@app.route("/")
def inicio():
    return render_template("formulario.html")

@app.route("/actualizar", methods=["POST"])
def actualizar():
    global nombre_usuario
    nombre_usuario = request.form["nombre"]
    return f"Nombre actualizado a {nombre_usuario}"

if __name__ == "__main__":
    app.run(debug=True)