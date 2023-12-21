
def return_nth_smallest_ascii(s):
    s = s[48:77]
    s = sorted(s, key=ord)
    return s[4]
