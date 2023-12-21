
def return_n_greatest_chars(s):
    if len(s) < 77:
        raise ValueError("The string should contain at least 77 distinct characters.")
    sorted_chars = sorted(s, key=ord, reverse=True)
    return sorted_chars[:77]
