import string
import secrets

def generate_password(length: int, symbols: bool, uppercase: bool):
    """
    Generates random passwords according to users preferences.

    length: Size in characters of the password.
    symbols: If you want symbols in your password.
    uppercase: If you want uppercased characters in your password.

    For best security we recommended a 17 characters with symbold and uppercase password.
    Check https://www.security.org/how-secure-is-my-password/ for more details.
    """
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    
    return new_password

# Change range() value to generate as many passwords you prefer
for _, index in enumerate(range(5)):
    
    print(index + 1, ":", generate_password(length=24, symbols=True, uppercase=True))