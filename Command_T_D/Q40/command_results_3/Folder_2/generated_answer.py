def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: x.lower())[:48]
