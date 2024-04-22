# create_tables.py

from app import app, db

# Create an application context
with app.app_context():
    # Now you can use Flask extensions safely
    db.create_all()
    print("Tables created successfully!")
