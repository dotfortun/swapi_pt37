from app import app
from api.models import User, db
import json

from tqdm import tqdm

users = []

with open('./src/users.json', 'rt') as user_file:
    users = json.load(user_file).get("results", [])

with app.app_context():
    for user in tqdm(users):
        db.session.add(
            User(
                email=user["email"],
                password=user["login"]["password"]
            )
        )
    db.session.commit()
