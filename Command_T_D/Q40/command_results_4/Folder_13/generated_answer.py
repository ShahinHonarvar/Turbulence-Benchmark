def return_n_smallest_chars(s):
    return sorted(s, key=str.isalpha)[-31:]
