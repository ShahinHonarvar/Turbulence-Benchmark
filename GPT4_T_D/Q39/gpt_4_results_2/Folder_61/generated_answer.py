
def return_n_greatest_chars(chars):
    if len(chars) < 66:
        raise ValueError("Input string should contain at least 66 distinct characters.")
    sorted_chars = sorted(chars, key=ord, reverse=True)
    return sorted_chars[:66]
