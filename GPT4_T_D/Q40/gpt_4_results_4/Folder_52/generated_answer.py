
def return_n_smallest_chars(chars):
    chars_list = list(chars)
    chars_list.sort()
    smallest_chars = chars_list[:68]
    return smallest_chars
