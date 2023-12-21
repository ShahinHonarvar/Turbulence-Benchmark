
def return_n_smallest_chars(s):
    list_chars = sorted(list(s), key=ord)[:83]
    return list_chars
