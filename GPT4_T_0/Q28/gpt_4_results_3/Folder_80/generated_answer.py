
def return_nth_smallest_ascii(s):
    s = s[51:90]
    s = sorted(s, key=ord)
    return s[13]
