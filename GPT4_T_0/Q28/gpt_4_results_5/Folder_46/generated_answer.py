
def return_nth_smallest_ascii(s):
    s = s[34:86]
    s = sorted(s, key=ord)
    return s[19]
