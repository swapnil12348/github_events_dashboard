import os
from dotenv import load_dotenv

# The basedir is the root of your project, where config.py lives.
basedir = os.path.abspath(os.path.dirname(__file__))

# --- THIS IS THE FIX ---
# Look for the .env file in the SAME directory as this config file.
# We have removed the '..' which was causing it to look in the wrong place.
env_path = os.path.join(basedir, '.env.development.local')

print("--- Running config.py ---")
print(f"--- Attempting to load .env file from: {env_path} ---")

if os.path.exists(env_path):
    print("--- .env file FOUND. Loading... ---")
    load_dotenv(dotenv_path=env_path, override=True)
else:
    print("--- .env file NOT FOUND. ---")

DATABASE_URL_FROM_ENV = os.environ.get('DATABASE_URL')
print(f"--- After attempting to load, os.environ.get('DATABASE_URL') is: {DATABASE_URL_FROM_ENV} ---")


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key-for-dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URL_FROM_ENV or \
                              'sqlite:///' + os.path.join(basedir, 'site.db')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = DATABASE_URL_FROM_ENV

    # This check is still important
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}