from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Config è una classe per indicare in quale ambiente stiamo lavorando


    #importo tutti i bp dentro routes
    #ogni bp è una relazione con le funzionalità del software
    from .routes import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app
