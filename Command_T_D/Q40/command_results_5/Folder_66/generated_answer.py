def return_n_smallest_chars(str):
    return [c for c in str if ord(c) < 33]
