import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Example
print(generate_password())  # e.g., "K9#mQ2$vLpX!"
