from flask import Flask
from .config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configura la sessione per logout al chiusura del browser
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_TYPE'] = 'filesystem'

    # db.init_app(app)
    # migrate.init_app(app, db)

    #importo tutti i bp dentro routes
    #ogni bp è una relazione con le funzionalità del software
    from .routes import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app
