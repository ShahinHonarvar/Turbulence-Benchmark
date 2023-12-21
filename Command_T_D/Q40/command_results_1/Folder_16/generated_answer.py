def return_n_smallest_chars(s):
    return sorted(set(s), key=lambda c: ord(c))[:64]
