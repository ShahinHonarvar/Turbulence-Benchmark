
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)[:44]
    return sorted_chars
