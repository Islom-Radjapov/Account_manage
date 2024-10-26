import random
import string

def generate_password(length=8):

    # Define character sets based on the requirements
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    #special_characters = "!@$%_#"

    # Ensure the password contains at least one character from each required set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(numbers),
        #random.choice(special_characters)
    ]

    # Fill the remaining length with random choices from allowed characters
    allowed_characters = lowercase_letters + uppercase_letters + numbers #+ special_characters
    password += random.choices(allowed_characters, k=length - 4)

    # Shuffle to ensure random order and join to create the password string
    random.shuffle(password)
    print(''.join(password))
    return ''.join(password)
generate_password(11)