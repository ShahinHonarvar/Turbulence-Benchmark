
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)
    n = min(len(chars), 45)
    return sorted_chars[:n]
