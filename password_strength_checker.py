import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase and lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1

    # Digit
    if re.search(r'\d', password):
        score += 1

    # Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Determine strength
    if score == 4:
        return "Strong", score
    elif score == 3:
        return "Medium", score
    else:
        return "Weak", score


if __name__ == "__main__":
    print("Password Strength Checker - Automated Test Cases\n")

    test_passwords = ["abc123", "Geeta123", "Geeta@123"]

    for pwd in test_passwords:
        strength, score = check_password_strength(pwd)
        print(f"Password: {pwd}")
        print(f"Password Strength: {strength} (Score: {score}/4)\n")
