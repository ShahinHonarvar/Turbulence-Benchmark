
def return_n_smallest_chars(chars):
    chars_list = list(chars)
    sorted_chars = sorted(chars_list, key=ord)
    return sorted_chars[:11]
