def return_n_smallest_chars(s):
    return sorted(set(s)[:13], key=lambda c: c.lower())
