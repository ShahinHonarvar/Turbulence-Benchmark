
def return_n_smallest_chars(s):
    if len(s) < 21:
        raise ValueError('The input string should contain at least 21 distinct characters.')
    chars = list(s)
    chars.sort(key=ord)
    return chars[:21]
