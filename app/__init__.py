from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='../static', static_url_path='')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)

    from app import routes
    app.register_blueprint(routes.bp)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app