
def return_n_smallest_chars(chars):
    chars = sorted(chars)[:35]
    return sorted(chars, reverse=True)
