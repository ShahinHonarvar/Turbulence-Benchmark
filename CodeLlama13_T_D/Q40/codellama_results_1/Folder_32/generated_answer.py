
def return_n_smallest_chars(string):
    chars = sorted(set(string), key=ord)
    return chars[:8]
