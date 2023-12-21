def return_n_smallest_chars(s):
    lst = sorted(s, key=lambda x: ord(x))[:65]
    return lst
