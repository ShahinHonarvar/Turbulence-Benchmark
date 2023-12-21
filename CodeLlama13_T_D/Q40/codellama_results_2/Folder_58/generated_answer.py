
def return_n_smallest_chars(string):
    chars = sorted(set(string), key=ord)[:49]
    return chars[::-1]
