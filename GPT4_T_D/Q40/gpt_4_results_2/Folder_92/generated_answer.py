
def return_n_smallest_chars(chars):
    chars_list = list(chars)
    chars_list.sort(key=ord)
    return chars_list[:63]
