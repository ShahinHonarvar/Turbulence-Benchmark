
def return_n_greatest_chars(chars):
    if len(set(chars)) != len(chars):
        raise ValueError("All characters in the string must be distinct")
    if len(chars) < 68:
        raise ValueError("The string must contain at least 68 characters")
    sorted_chars = sorted(chars, reverse=True)
    return sorted_chars[:68]
