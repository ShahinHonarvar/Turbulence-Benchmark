
def return_n_smallest_chars(s):
    chars = sorted(set(s), key=ord)[:33]
    return list(reversed(chars))
