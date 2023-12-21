
def return_n_smallest_chars(string):
    chars = sorted(list(set(string)), key=ord)[:61]
    return chars[::-1]
