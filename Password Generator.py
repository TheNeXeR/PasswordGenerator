import string
import random


# Designed and programmed with Love "NeXeR"
# Fast - Secure 
# High-Level Password under 1s
# Https://t.me/TheNeXeR


def passwordGenerator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
#------------------------------------------------------------------------
def saveThePassword(password):
    try:
        with open("password.txt", "w") as file:
            file.write(password)
        print("Password saved to 'password.txt' successfully.")
    except Exception as e:
        print(f"An error occurred while saving the password: {e}")
#------------------------------------------------------------------------
def generate():
    try:
        length = int(input("Enter the length of the password (Between 8/32): "))
        if length < 8 or length > 32:
            print("Password length must be between 8 and 32 characters.")
            return
        password = passwordGenerator(length)
        print(f"Generated password: {password}")
        saveThePassword(password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")
#------------------------------------------------------------------------
generate()