
def return_nth_smallest_ascii(s):
    s = s[:16]
    s = sorted(s, key=ord)
    return s[15]
