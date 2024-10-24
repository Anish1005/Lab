import hashlib
import hmac
import os

def generate_salt(length=16):
    return os.urandom(length)

def hash_password(password, salt):
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return password_hash

def create_hmac(key, message):
    h = hmac.new(key, message.encode('utf-8'), hashlib.sha256)
    return h.digest()

def main():
    password = "Anish"
    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    print("Password:", password)
    print("Salt:", salt)
    print("Hashed Password:", hashed_password.hex())

    secret_key = b'secret_key'
    message = "Hello, HMAC!"
    hmac_result = create_hmac(secret_key, message)
    print("HMAC:", hmac_result.hex())

if __name__ == "__main__":
    main()
