def return_n_smallest_chars(s):
    return sorted(s, key=lambda c: c.lower())[:56]
