import random
import string

def generate_password(length):
    """Generate a password with a mix of letters, digits, and special characters"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
try:
    length = int(input("Enter the desired password length: "))
    if length < 4:
        print("Password length should be at least 4 characters for security.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number!")
