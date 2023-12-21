
def return_nth_smallest_ascii(s):
    s = s[17:57]
    s = sorted(s, key=ord)
    return s[8]
