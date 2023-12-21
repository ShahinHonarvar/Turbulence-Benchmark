
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    smallest_chars = sorted_chars[:54]
    return smallest_chars[::-1]
