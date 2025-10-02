# Rotate list left by n positions
def rotate_left(lst, n):
    return lst[n:] + lst[:n]

# Rotate list right by n positions
def rotate_right(lst, n):
    n = n % len(lst)  # Handle large n
    return lst[-n:] + lst[:-n]

# Example
nums = [1, 2, 3, 4, 5]
print(rotate_left(nums, 2))   # [3, 4, 5, 1, 2]
print(rotate_right(nums, 2))  # [4, 5, 1, 2, 3]
