
def return_nth_smallest_ascii(s):
    s = s[62:84]
    s = sorted(s, key=ord)
    return s[8]
