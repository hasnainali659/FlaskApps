from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "Hasnain"

hashed_password = bcrypt.generate_password_hash(password)

check_password = bcrypt.check_password_hash(hashed_password, password)
print(check_password)