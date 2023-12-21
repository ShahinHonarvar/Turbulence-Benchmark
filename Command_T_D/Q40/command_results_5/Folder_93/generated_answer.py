def return_n_smallest_chars(str):
    return list(sorted(set(str), key=str.index))[:77]
