def return_n_smallest_chars(str_arg):
    res = sorted(str_arg, key=lambda x: ord(x))[:34]
    return res
