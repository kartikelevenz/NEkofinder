import random

def random_hex_color():
    """Generate a random hex color like #a3f2b1"""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

# Example
print(random_hex_color())  # e.g., #4e8c2a
