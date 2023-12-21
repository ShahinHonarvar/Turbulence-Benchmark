def return_n_smallest_chars(s):
    return [x for x in sorted(s) if ord(x) < 1000]
