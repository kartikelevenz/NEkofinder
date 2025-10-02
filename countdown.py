import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\rTime left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ Time's up!")

# Example (5-second timer)
countdown(5)
