def return_n_smallest_chars(s):
    res = sorted(set(s), key=lambda x: ord(x))[:49]
    return res
