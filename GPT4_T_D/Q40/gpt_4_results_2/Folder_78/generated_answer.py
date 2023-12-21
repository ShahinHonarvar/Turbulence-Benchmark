
def return_n_smallest_chars(s):
    smallest_chars = sorted(list(s), key=ord)[:43]
    return sorted(smallest_chars, reverse=True)
