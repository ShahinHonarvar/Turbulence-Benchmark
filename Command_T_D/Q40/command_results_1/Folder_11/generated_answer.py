def return_n_smallest_chars(s):
    res = sorted(s, key=str.lower)[:17]
    return res
