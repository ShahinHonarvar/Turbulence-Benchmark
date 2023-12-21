
def return_n_greatest_chars(chars):
    if len(chars) < 43:
        return "Error: String length should be at least 43 distinct characters."

    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[-43:]
