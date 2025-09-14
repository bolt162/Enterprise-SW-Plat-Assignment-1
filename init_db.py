# init_db.py
from hangman import db, create_app

app = create_app()   # or import your app object - adjust if different

with app.app_context():
    db.create_all()
    print("DB created")
