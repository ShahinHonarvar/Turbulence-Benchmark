
def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=ord)[:27]
    return sorted(smallest_chars, reverse=True)
