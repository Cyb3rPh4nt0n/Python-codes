#Passwords Generator

import string
import random
import secrets

longuitud = int(input("Indicates the desired length for the password: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = []

while len(contraseña) < longuitud:
    contraseña.append(secrets.choice(caracteres))

random.shuffle(contraseña)
contraseña = "".join(contraseña)

print(f"Your password is: {contraseña}")