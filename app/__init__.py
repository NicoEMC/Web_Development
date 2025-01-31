from flask import Flask
from flask_session import Session

def create_app():
    """
    Configura e inicia la aplicación Flask.

    Returns:
        Flask: Aplicación Flask configurada.
    """
    app = Flask(__name__)
    app.secret_key = "supersecretkey"  # Cambiar por una clave más segura en producción
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Registrar Blueprints
    from app.routes import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    return app
