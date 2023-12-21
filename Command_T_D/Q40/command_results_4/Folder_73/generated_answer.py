def return_n_smallest_chars(str_arg):
    return sorted(str_arg, key=lambda x: ord(x))[:80]
