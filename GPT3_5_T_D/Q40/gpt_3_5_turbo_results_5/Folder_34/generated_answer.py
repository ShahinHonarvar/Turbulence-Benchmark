
def return_n_smallest_chars(s):
    chars = sorted(list(s))
    return chars[:9][::-1]
