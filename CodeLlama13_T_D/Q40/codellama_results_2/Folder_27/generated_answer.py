
def return_n_smallest_chars(string):
    chars = sorted(set(string), key=ord)[:82]
    return list(chars)
