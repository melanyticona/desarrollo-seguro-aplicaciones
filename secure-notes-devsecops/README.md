# SecureNotes - DevSecOps

Plataforma segura para almacenar notas financieras.

## Instalacion

1. Clonar repositorio
2. python -m venv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt
5. python app.py

## Usar la aplicacion

1. Ve a http://localhost:5000
2. Registra un usuario
3. Inicia sesion
4. Entra al dashboard

## Requisitos

- Python 3.10
- MySQL Server
- pip

## Seguridad

- Contrasenas encriptadas con Werkzeug
- Proteccion CSRF con Flask-WTF
- SQL parametrizado (sin SQL Injection)
- Validacion de formularios con WTForms
- Sesiones seguras con Flask-Login

## Archivos principales

- app.py: Aplicacion Flask
- db.py: Conexion MySQL
- models.py: Funciones de BD
- forms.py: Formularios
- init_db.py: Crea BD automaticamente
- requirements.txt: Dependencias
- .env: Variables de entorno