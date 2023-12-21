
def return_n_smallest_chars(s):
    chars = sorted(set(s))
    return sorted([c for c in chars if ord(c) < 63], key=ord)[:63]
