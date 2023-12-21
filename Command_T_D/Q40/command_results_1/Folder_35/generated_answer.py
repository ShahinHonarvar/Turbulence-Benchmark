def return_n_smallest_chars(s):
    return [c for c in sorted(set(s)) if len(list(filter(lambda x: x == c, s))) == 1]
