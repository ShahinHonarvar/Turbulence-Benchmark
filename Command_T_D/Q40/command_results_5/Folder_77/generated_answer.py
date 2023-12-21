def return_n_smallest_chars(s):
    lst = sorted(set(s), key=str.lower)[:47]
    return lst
