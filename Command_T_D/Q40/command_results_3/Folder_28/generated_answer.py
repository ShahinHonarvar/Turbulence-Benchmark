def return_n_smallest_chars(s):
    return [i for i in s if i in sorted(s)[-3:]]
