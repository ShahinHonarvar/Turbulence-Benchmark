def return_n_smallest_chars(s):
    res = sorted(s, key=lambda c: ord(c))[:13]
    return res
