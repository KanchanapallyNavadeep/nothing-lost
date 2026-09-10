import json
import os
import hashlib
import secrets


USERS_FILE = os.path.join(
    os.path.dirname(__file__),
    "users.json"
)


def load_users():

    if not os.path.exists(USERS_FILE):

        return []


    with open(
        USERS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_users(users):

    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            users,
            file,
            indent=4
        )



def hash_password(password, salt=None):

    if salt is None:

        salt = secrets.token_hex(16)


    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000
    )


    return (
        salt,
        password_hash.hex()
    )



def verify_password(password, salt, stored_hash):

    _, password_hash = hash_password(
        password,
        salt
    )


    return secrets.compare_digest(
        password_hash,
        stored_hash
    )



def register_user(
    email,
    password,
    role="user"
):

    users = load_users()


    for user in users:

        if user["email"].lower() == email.lower():

            return None


    salt, password_hash = hash_password(
        password
    )


    user = {

        "id": len(users) + 1,

        "email": email,

        "password_hash": password_hash,

        "salt": salt,

        "role": role

    }


    users.append(user)

    save_users(users)


    return user



def authenticate_user(
    email,
    password
):

    users = load_users()


    for user in users:

        if user["email"].lower() == email.lower():

            if verify_password(
                password,
                user["salt"],
                user["password_hash"]
            ):

                return user


    return None