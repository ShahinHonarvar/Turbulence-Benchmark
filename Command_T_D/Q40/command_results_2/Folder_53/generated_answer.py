def return_n_smallest_chars(s):
    lst = list(sorted(set(s), key=lambda c: ord(c)))[:19]
    return lst
