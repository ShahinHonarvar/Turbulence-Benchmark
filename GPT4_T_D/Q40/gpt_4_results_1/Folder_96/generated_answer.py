
def return_n_smallest_chars(s):
    s = sorted(s, key=ord)
    s = s[:20]
    s.sort(reverse=True)
    return s
