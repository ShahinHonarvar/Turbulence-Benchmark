
def return_nth_smallest_ascii(s):
    s = s[:15]
    s = sorted(s, key=ord)
    return s[14]
