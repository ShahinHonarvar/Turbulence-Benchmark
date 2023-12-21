
def return_n_smallest_chars(s):
    chars = sorted(list(set(s)), key=lambda c: ord(c))
    return chars[:70]
