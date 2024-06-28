import bcrypt

class crypt_password():
    def __init__(self, password):
        self.password = password

    def hash(self):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        return hashed