
def return_n_smallest_chars(chars):
    sorted_chars = sorted(list(chars), key=ord)[:35]
    return sorted_chars[::-1]
