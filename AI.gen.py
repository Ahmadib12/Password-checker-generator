import string
import random

def check_password_strength_basic(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = 0
    reasons = []

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        reasons.append("Password is too short (less than 8 characters).")

    if has_upper:
        score += 1
    else:
        reasons.append("Password should contain uppercase letters.")

    if has_lower:
        score += 1
    else:
        reasons.append("Password should contain lowercase letters.")

    if has_digit:
        score += 1
    else:
        reasons.append("Password should contain digits.")

    if has_special:
        score += 1
    else:
        reasons.append("Password should contain special characters (e.g., !@#$%^&*).")

    if score >= 5 and length >= 12:
        strength = "Strong"
    elif score >= 3 and length >= 8:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, reasons

def generate_password(length=12, include_upper=True, include_lower=True, include_digits=True, include_special=True):
    """Generates a random password based on specified criteria."""
    characters = ''
    if include_upper:
        characters += string.ascii_uppercase
    if include_lower:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return "Error: At least one character type must be selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Check Password Strength")
        print("2. Generate Password")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            password_to_check = input("Enter the password you want to check: ")
            strength, reasons = check_password_strength_basic(password_to_check)
            print(f"\nPassword Strength: {strength}")
            if reasons:
                print("Suggestions:")
                for reason in reasons:
                    print(f"- {reason}")
        elif choice == '2':
            length_str = input("Enter the desired length of the password (default is 12): ")
            length = int(length_str) if length_str.isdigit() else 12

            include_upper_input = input("Include uppercase letters? (y/N): ").lower()
            include_upper = include_upper_input == 'y'

            include_lower_input = input("Include lowercase letters? (y/N): ").lower()
            include_lower = include_lower_input == 'y'

            include_digits_input = input("Include digits? (y/N): ").lower()
            include_digits = include_digits_input == 'y'

            include_special_input = input("Include special characters? (y/N): ").lower()
            include_special = include_special_input == 'y'

            generated_password = generate_password(length, include_upper, include_lower, include_digits, include_special)
            print(f"\nGenerated Password: {generated_password}")
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
