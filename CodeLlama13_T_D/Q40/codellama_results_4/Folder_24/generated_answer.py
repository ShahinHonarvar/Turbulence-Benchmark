
def return_n_smallest_chars(s):
    chars = sorted(s, key=ord)
    return chars[:32]
