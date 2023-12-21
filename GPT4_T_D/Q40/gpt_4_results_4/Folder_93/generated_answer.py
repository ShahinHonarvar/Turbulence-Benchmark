
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    smallest_chars = sorted_chars[:77]
    smallest_chars_desc = sorted(smallest_chars, reverse=True)
    return smallest_chars_desc
