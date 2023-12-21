
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    smallest_chars = sorted_chars[:26]
    smallest_chars.sort(reverse=True)
    return smallest_chars
