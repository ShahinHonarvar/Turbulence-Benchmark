
def return_n_greatest_chars(s):
    if len(s) < 90:
        raise ValueError("Input string should contain at least 90 distinct characters.")
    sorted_chars = sorted(s, reverse=True)
    return sorted_chars[:90]
