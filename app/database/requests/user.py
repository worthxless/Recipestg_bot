from app.database.database import SessionLocal
from app.database.models.user import User


def create_new_user(user_id, name, surname, username, number):
    with SessionLocal() as session:
        new_user = User()
        new_user.id = user_id
        new_user.name = name
        new_user.surname = surname
        new_user.username = username
        new_user.number = number
        session.add(new_user)
        session.commit()
    return True

def get_user(user_id):
    with SessionLocal() as session:
        user = session.query(User).get(user_id)
        return user