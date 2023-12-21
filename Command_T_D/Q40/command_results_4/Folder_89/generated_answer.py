def return_n_smallest_chars(str):
    res = sorted(set(str), key=lambda x: ord(x))[:55]
    return res
