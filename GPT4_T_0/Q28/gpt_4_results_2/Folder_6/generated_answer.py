
def return_nth_smallest_ascii(s):
    s = s[14:55]
    s = sorted(s, key=ord)
    return s[10]
