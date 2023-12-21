
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    first_55_chars = sorted_chars[:55]
    return first_55_chars
