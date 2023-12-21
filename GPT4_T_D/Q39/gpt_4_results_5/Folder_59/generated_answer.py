
def return_n_greatest_chars(s):
    if len(s) < 13:
        raise ValueError("The input string must have at least 13 characters")
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:13]
