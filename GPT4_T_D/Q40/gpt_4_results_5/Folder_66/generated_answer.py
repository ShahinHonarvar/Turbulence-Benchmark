
def return_n_smallest_chars(str_chars):
    sorted_chars = sorted(str_chars, key=ord)
    smallest_chars = sorted_chars[:33]
    smallest_chars.sort(reverse=True)
    return smallest_chars
