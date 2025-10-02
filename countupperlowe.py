def count_case(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    return {"uppercase": upper, "lowercase": lower}

# Example
result = count_case("Hello World!")
print(result)  # {'uppercase': 2, 'lowercase': 8}
