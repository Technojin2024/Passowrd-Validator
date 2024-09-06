# Input password from user
password = input("Enter a password to validate: ")

# Define the criteria
min_length = 8
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_characters = "!@#$%^&*()-+"

# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True

# Check if all criteria are met
if (len(password) >= min_length and has_upper and has_lower and has_digit and has_special):
    print("Password is valid.")
else:
    print("Password is invalid. Your password must include at least one uppercase letter, one lowercase letter, a number, and a special character.")
