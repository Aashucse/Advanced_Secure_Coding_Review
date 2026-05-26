import hashlib
import getpass
from datetime import datetime

# Stored credentials
stored_username = "admin"

# Password: Cyber@123
stored_password = hashlib.sha256("Cyber@123".encode()).hexdigest()

# Login attempts
attempts = 3

# Password strength checker
def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password"

    if not any(char.isupper() for char in password):
        return "Weak Password"

    if not any(char.islower() for char in password):
        return "Weak Password"

    if not any(char.isdigit() for char in password):
        return "Weak Password"

    return "Strong Password"

# Logging function
def log_attempt(username, status):
    with open("login_logs.txt", "a") as file:
        file.write(
            f"{datetime.now()} | Username: {username} | Status: {status}\n"
        )

print("=" * 50)
print("      ADVANCED SECURE LOGIN SYSTEM")
print("=" * 50)

while attempts > 0:

    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ")

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and hashed_password == stored_password:
        print("\nLogin Successful")
        log_attempt(username, "SUCCESS")
        break

    else:
        attempts -= 1
        print(f"\nInvalid Credentials")
        print(f"Attempts Left: {attempts}")

        log_attempt(username, "FAILED")

if attempts == 0:
    print("\nToo many failed attempts. Access blocked.")