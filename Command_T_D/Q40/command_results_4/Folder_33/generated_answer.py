def return_n_smallest_chars(str):
    smallest_chars = sorted(str, key=str.index)[:36]
    return smallest_chars
