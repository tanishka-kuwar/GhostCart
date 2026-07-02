from faker import Faker
import random

from app.extensions import db
from app.users.models import User

fake = Faker("en_IN")

def seed_users(count=1000):

    print(f"Generating {count} users...")

    users = []

    for i in range(count):
        user = User(
            username = fake.user_name() + str(random.randint(1000,9999)),
            email = fake.unique.email(),
            password_hash = "ghostcart123"
        )

        users.append(user)
    
    db.session.bulk_save_objects(users)
    db.session.commit()
    print(f"Inserted {count} users.")