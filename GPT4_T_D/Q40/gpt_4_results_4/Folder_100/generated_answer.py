
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    smallest_72_chars = sorted(sorted_chars[:72], reverse=True)
    return smallest_72_chars
