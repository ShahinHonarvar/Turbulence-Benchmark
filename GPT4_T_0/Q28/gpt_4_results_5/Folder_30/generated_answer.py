
def return_nth_smallest_ascii(s):
    s = s[50:77]
    s = sorted(s, key=ord)
    return s[10]
