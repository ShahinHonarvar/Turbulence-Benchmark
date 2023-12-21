
def return_n_smallest_chars(arg):
    sorted_chars = sorted(arg, key=ord)
    n_smallest_chars = sorted_chars[:65]
    return list(sorted(n_smallest_chars, reverse=True))
