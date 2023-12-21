
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)
    smallest_chars = sorted_chars[:13]
    descending_smallest_chars = sorted(smallest_chars, reverse=True)
    return descending_smallest_chars
