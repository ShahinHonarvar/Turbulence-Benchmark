
def return_nth_smallest_ascii(s):
    s = s[4:34]
    s = sorted(s, key=ord)
    return s[3]
