
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    smallest_chars = s[:77]
    return sorted(smallest_chars, reverse=True)
