
def return_nth_smallest_ascii(s):
    s = s[10:74]
    s = sorted(s, key=ord)
    return s[8]
