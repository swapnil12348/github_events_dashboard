# create_tables.py
from app import create_app, db

# No need for load_dotenv here anymore, config.py does it!

# Use the 'production' config to ensure it uses the production database URL
app = create_app('production')

# The 'with' statement ensures the application context is active
with app.app_context():
    print("Creating database tables...")
    # This command creates all tables defined in your models
    db.create_all()
    print("Tables created successfully!")