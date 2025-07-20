# import re

# # password strength check condition:
# # min 8 chars, digit, uppercase, lowercase, special character
# def check_password_strength(password):
#     if len(password) < 8:
#         return "Weak: Password must be at least 8 characters"
#     if not any(char.isdigit() for char in password):
#         return "Weak: Password must contain a digit"
#     if not any(char.isupper() for char in password):
#         return "Weak: Password must contain an uppercase character"
#     if not any(char.islower() for char in password):
#         return "Weak: Password must contain a lowercase character"
#     if not re.search(r'[!@#$%^&*()<>_\-?/+]', password):
#         return "Medium: Password should contain a special character"
    
#     return "Strong: Your password is secure!"

# def password_checker():
#     print("Welcome to the Password Strength Checker")

#     while True:
#         password = input("Enter your password (or type 'exit' to quit): ")

#         if password.lower() == 'exit':
#             print("Thank you for using this tool!")
#             break

#         result = check_password_strength(password)
#         print(result)

# if __name__ == "__main__":
#     password_checker()

import math
import re

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'\d', password):
        charset += 10
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password):
        charset += 32

    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

def estimate_crack_time(entropy):
    # Assume 1 billion guesses per second
    guesses = 2 ** entropy
    seconds = guesses / 1e9

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    else:
        return f"{seconds / 31536000:.2f} years"

def test_password_strength(password):
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    if entropy < 28:
        strength = "Very Weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Reasonable"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, entropy, crack_time

def run_password_tester():
    print(" Welcome to the Password Strength Tester")

    while True:
        password = input("\nEnter a password to test (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print(" Thank you for using the Password Strength Tester!")
            break

        strength, entropy, crack_time = test_password_strength(password)
        print(f"Entropy: {entropy:.2f} bits")
        print(f"Estimated crack time: {crack_time}")
        print(f"Strength Rating: {strength}")

if __name__ == "__main__":
    run_password_tester()
