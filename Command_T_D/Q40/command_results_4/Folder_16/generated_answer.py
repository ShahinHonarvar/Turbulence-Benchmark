def return_n_smallest_chars(s):
    return [c for c in sorted(set(s)) if ord(c) < 64]
