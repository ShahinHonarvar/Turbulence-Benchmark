def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: ord(x))[:47]
