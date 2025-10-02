def is_palindrome(s):
    """Check if a string reads the same backward as forward (ignores case & spaces)."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Example
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))                        # False
