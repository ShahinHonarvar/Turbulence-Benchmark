
def return_n_smallest_chars(s):
    chars = sorted(set(s), key=ord)[:7]
    return chars[::-1]
