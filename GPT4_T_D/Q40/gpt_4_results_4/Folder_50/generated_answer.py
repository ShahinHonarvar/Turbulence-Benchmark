
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)[:16]
    s.sort(reverse=True)
    return s
