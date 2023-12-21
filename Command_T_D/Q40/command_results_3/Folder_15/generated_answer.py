def return_n_smallest_chars(s):
    return [c for c in s if ord(c) in range(ord("A") + 1, ord("z") + 1)]
