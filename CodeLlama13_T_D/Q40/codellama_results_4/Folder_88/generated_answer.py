
def return_n_smallest_chars(string):
    chars = sorted(list(set(string)), key=ord)
    return chars[:84]
