export FLASK_APP=app.py

flask db init        # Initialize the migrations directory
flask db migrate -m "Initial migration."
flask db upgrade     # Apply the migration to the database
