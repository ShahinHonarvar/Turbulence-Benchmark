
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars)
    n = min(19, len(sorted_chars))
    return sorted_chars[-n:]
