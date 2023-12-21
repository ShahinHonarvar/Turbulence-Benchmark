
def return_nth_smallest_ascii(s):
    s = s[24:72]
    s = sorted(s, key=ord)
    return s[7]
