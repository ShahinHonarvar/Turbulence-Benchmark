
def return_n_smallest_chars(str):
    str_sorted = sorted(str, key=ord)
    return str_sorted[:29]
