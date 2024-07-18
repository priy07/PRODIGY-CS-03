import re

def password_strength(password):
    strength = 0
    feedback = []

    # Length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    elif len(password) >= 12:
        strength += 1
        feedback.append("Good job! Password is long enough.")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
        feedback.append("Good job! Password contains uppercase letters.")
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
        feedback.append("Good job! Password contains lowercase letters.")
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Numbers
    if re.search(r"\d", password):
        strength += 1
        feedback.append("Good job! Password contains numbers.")
    else:
        feedback.append("Password should contain at least one number.")

    # Special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
        feedback.append("Good job! Password contains special characters.")
    else:
        feedback.append("Password should contain at least one special character.")

    # Password strength rating
    if strength < 2:
        feedback.append("Password is weak. Try to improve it!")
    elif strength == 2:
        feedback.append("Password is medium strength. Good, but can be better!")
    else:
        feedback.append("Password is strong! Well done!")

    return feedback

def main():
    password = input("Enter a password: ")
    feedback = password_strength(password)
    for message in feedback:
        print(message)

if __name__ == "__main__":
    main()