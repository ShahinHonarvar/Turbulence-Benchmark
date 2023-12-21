
def return_n_greatest_chars(s):
    if len(s) < 23:
        raise ValueError("The string should contain at least 23 distinct characters")
    sorted_s = sorted(s, key=ord, reverse=True)
    return sorted(sorted_s[:23])
