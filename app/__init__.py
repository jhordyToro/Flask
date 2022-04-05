from flask import Flask
from flask_bootstrap import Bootstrap # es una libreria de Flask que nos permite decorar mas nuestro sitio web con su propia sintaxis
from .config import Config

def Create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app) # asi se inicializa BootsTrap

    app.config.from_object(Config)
    return app