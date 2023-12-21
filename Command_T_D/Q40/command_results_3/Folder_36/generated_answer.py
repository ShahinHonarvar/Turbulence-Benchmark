def return_n_smallest_chars(s):
    return list(sorted(s, key=lambda c: ord(c)))[:32]
