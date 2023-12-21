
def return_n_smallest_chars(chars):
    n = min(36, len(chars))
    return sorted(chars)[:n][::-1]
