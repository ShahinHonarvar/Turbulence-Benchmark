
def return_n_smallest_chars(s):
    s_sorted = sorted(s, key=ord)
    return s_sorted[:44]
