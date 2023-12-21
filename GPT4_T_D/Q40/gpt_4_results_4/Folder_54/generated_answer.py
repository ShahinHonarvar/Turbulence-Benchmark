
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    n_smallest_chars = s[:79]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars
