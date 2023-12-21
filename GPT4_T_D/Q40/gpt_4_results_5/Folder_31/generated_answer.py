
def return_n_smallest_chars(s):
    s = sorted(s, key=ord, reverse=True)
    return s[:70]
