from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import re


class UsernameValidator:
    def __call__(self, form, field):
        if not re.match(r'^[a-zA-Z0-9_]+$', field.data):
            raise ValidationError('El usuario solo puede contener letras, numeros y guiones bajos.')


class LoginForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[
            DataRequired(message="El usuario es requerido"),
            Length(min=3, max=50, message="Entre 3 y 50 caracteres"),
            UsernameValidator()
        ]
    )

    password = PasswordField(
        "Contrasena",
        validators=[
            DataRequired(message="La contrasena es requerida"),
            Length(min=4, max=100, message="Entre 4 y 100 caracteres")
        ]
    )

    submit = SubmitField("Ingresar")


class RegisterForm(FlaskForm):
    username = StringField(
        "Usuario",
        validators=[
            DataRequired(message="El usuario es requerido"),
            Length(min=3, max=50, message="Entre 3 y 50 caracteres"),
            UsernameValidator()
        ]
    )

    password = PasswordField(
        "Contrasena",
        validators=[
            DataRequired(message="La contrasena es requerida"),
            Length(min=4, max=100, message="Entre 4 y 100 caracteres")
        ]
    )

    submit = SubmitField("Registrar")