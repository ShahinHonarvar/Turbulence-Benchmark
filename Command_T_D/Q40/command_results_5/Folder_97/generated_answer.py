def return_n_smallest_chars(str):
    res = sorted(str, key=lambda x: ord(x))[:38]
    return res
