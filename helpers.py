import random
import string

def generate_random_string(length):
    # Define the possible characters to include: uppercase, lowercase, and digits
    characters = string.ascii_letters + string.digits
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
