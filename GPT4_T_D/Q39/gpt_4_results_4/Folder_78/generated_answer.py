
def return_n_greatest_chars(chars):
    if len(set(chars)) != len(chars):
        raise ValueError("The string must contain distinct characters.")
    sorted_chars = sorted(chars, key=ord, reverse=True)
    return sorted_chars[:43]
