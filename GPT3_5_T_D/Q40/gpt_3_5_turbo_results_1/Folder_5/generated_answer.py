
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)
    n_smallest_chars = sorted_chars[:46]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars
