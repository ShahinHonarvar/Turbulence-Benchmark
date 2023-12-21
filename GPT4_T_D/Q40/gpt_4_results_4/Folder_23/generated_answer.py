
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[:46]
