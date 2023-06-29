USERS = {
    "user1": "password1",
    "user2": "password2",
}

def is_registered(username):
    return username in USERS

def authenticate(username, password):
    return USERS.get(username) == password