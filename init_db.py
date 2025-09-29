# init_db.py
from hangman import db, app

with app.app_context():
    db.create_all()
    print("DB created")
