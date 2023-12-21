def return_n_smallest_chars(s):
    return [min(s, key=lambda x: ord(x)) for i in range(len(s) - 1)]
