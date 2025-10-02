import random

def safe_choice(items):
    if not items:
        return None
    return random.choice(items)

# Example
colors = ['red', 'green', 'blue']
print(safe_choice(colors))  # e.g., "green"
print(safe_choice([]))      # None (no crash!)
