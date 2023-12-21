def return_n_smallest_chars(s):
    return sorted(set(s), key=lambda x: ord(x))[:90]
