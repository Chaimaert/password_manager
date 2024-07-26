import hashlib # to hash the password
import getpass # to hide the password from the user

password_manager = {}

def create_account():
  username = input("Enter your desired username: ")
  password = getpass.getpass("Enter your desired password:")
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  password_manager[username] = hashed_password
  print("Account created successfully")