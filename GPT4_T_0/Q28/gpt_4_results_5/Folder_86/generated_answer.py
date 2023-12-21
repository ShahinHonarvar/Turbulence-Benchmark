
def return_nth_smallest_ascii(s):
    s = s[44:70]
    s = sorted(s, key=ord)
    return s[14]
