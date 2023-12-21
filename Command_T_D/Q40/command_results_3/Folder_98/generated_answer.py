def return_n_smallest_chars(s):
    return sorted(s, key=str.islower)[-68:]
