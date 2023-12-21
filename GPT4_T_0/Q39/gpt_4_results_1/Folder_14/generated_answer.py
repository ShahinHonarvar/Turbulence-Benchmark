
def return_n_greatest_chars(s):
    if len(s) < 69:
        raise ValueError("The string should contain at least 69 distinct characters.")
    sorted_chars = sorted(s, key=ord, reverse=True)[:69]
    return sorted(sorted_chars)
