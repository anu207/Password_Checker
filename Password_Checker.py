import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Lowercase
    if re.search("[a-z]", password):
        score += 1

    # Uppercase
    if re.search("[A-Z]", password):
        score += 1

    # Numbers
    if re.search("[0-9]", password):
        score += 1

    # Special characters
    if re.search("[@#$%^&*]", password):
        score += 1

    # Result
    if score <= 2:
        return "Weak ❌"
    elif score == 3 or score == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

# User input
password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)