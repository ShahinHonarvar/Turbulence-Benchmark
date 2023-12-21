
def return_n_smallest_chars(chars):
    smallest_chars = sorted(chars)[:2]
    return sorted(smallest_chars, reverse=True)
