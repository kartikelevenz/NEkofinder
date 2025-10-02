def factorial(n):
    """Return factorial of n (n!). Raises error for negative input."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example
print(factorial(5))  # 120
