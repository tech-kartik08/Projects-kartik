import re

# password strength check condition:
# min 8 chars, digit, uppercase, lowercase, special character
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain a digit"
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain an uppercase character"
    if not any(char.islower() for char in password):
        return "Weak: Password must contain a lowercase character"
    if not re.search(r'[!@#$%^&*()<>_\-?/+]', password):
        return "Medium: Password should contain a special character"
    
    return "Strong: Your password is secure!"

def password_checker():
    print("Welcome to the Password Strength Checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool!")
            break

        result = check_password_strength(password)
        print(result)

if __name__ == "__main__":
    password_checker()
