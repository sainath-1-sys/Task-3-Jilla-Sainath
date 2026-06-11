import random
import string

print("=== SECURE PASSWORD GENERATOR ===")

try:
    length = int(input("Enter password length (minimum 4): "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("!@#$%^&*")
        ]

        all_chars = string.ascii_letters + string.digits + "!@#$%^&*"

        for i in range(length - 4):
            password.append(random.choice(all_chars))

        random.shuffle(password)

        print("\nGenerated Password:")
        print("".join(password))

except ValueError:
    print("Please enter a valid number only.")