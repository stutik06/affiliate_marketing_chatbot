import bcrypt
from database import get_user, create_user

def signup_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return create_user(username, hashed.decode())

def login_user(username, password):
    user = get_user(username)
    if user and bcrypt.checkpw(password.encode(), user.password.encode()):
        return True
    return False

