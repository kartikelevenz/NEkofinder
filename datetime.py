from datetime import datetime

def current_timestamp(fmt="%Y-%m-%d %H:%M:%S"):
    """Return current time as a formatted string."""
    return datetime.now().strftime(fmt)

# Example
print(current_timestamp())           # 2024-10-05 14:30:45
print(current_timestamp("%d/%m/%Y")) # 05/10/2024
