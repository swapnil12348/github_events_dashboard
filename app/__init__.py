# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import config  # Your config dictionary

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'routes.login'

def create_app(config_name=None):
    """Application factory function."""
    app = Flask(__name__)

    # --- Vercel-friendly Config Selection ---
    if config_name is None:
        # Vercel sets VERCEL_ENV to 'production', 'preview', or 'development'
        # Default to 'development' for local runs
        config_name = os.environ.get('VERCEL_ENV') or 'development'
        
    # Load configuration from our config object
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize extensions with the app
    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)  # Enable CORS for all API routes

    # Import and register the blueprint from routes.py
    from . import routes
    app.register_blueprint(routes.bp, url_prefix='/api') # IMPORTANT: Add an API prefix

    # You can now REMOVE the catch_all route. Vercel will handle this.
    # The 'vercel.json' file will take care of serving static files
    # and routing all other requests correctly.

    # This is for Flask-Login to find the User model
    from . import models
    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))

    return app

# --- This is the most important part for Vercel ---
# Create the app instance at the top level of the file
# Vercel will look for this 'app' object.
app = create_app()
