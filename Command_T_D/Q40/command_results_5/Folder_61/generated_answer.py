def return_n_smallest_chars(s):
    res = sorted(s, key=lambda x: ord(x))[:66]
    return res
