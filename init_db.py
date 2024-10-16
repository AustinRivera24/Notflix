# init_db.py
from app import db, app  # Ensure you're importing both the app and db

# Use the app context to initialize the database
with app.app_context():
    db.create_all()
    print("Database initialized!")
