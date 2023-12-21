def return_n_smallest_chars(s):
    res = sorted(s, key=str.ascii_lowercase.index)[:23]
    return res
