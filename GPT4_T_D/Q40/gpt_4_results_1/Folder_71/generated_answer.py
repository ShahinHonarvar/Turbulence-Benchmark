
def return_n_smallest_chars(s):
    if len(s) < 14:
        raise ValueError("Input string must have at least 14 distinct characters")
    return sorted(list(s))[:14]
