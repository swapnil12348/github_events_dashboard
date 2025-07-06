import os
from app import create_app

# Use the FLASK_CONFIG environment variable, defaulting to 'development'
config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)

if __name__ == '__main__':
    # The 'with' statement is not needed here as db operations should
    # be handled by migrations or a one-time script, not on every run.
    app.run(debug=True)
