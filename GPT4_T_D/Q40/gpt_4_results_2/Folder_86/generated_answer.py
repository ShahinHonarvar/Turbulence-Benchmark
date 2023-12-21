
def return_n_smallest_chars(s):
    s = list(s)
    s.sort(key = ord)
    return s[:34]
