
def return_n_smallest_chars(string):
    chars = sorted(set(string), key=ord)[:39]
    return chars[::-1]
