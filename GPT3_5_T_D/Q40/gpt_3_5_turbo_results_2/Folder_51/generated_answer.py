
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)
    n_smallest_chars = sorted_chars[:45]
    return sorted(n_smallest_chars, reverse=True)
