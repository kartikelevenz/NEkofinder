def flatten(lst):
    """Flatten any nested list into a single-level list."""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Example
nested = [1, [2, [3, 4], 5], 6]
print(flatten(nested))  # [1, 2, 3, 4, 5, 6]
