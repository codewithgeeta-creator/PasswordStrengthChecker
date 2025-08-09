
import re
import getpass

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score == 4:
        return "Strong", score
    elif score == 3:
        return "Medium", score
    else:
        return "Weak", score

if __name__ == "__main__":
    print("Password Strength Checker")
    pwd = getpass.getpass("Enter your password (input hidden): ")
    strength, score = check_password_strength(pwd)
    print(f"Password Strength: {strength} (Score: {score}/4)")
