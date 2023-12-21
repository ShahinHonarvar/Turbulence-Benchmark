
def return_n_smallest_chars(chars):
    return sorted(list(chars), key=ord)[:9][::-1]
