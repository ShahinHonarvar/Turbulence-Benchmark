
def return_nth_smallest_ascii(s):
    s = s[25:46]
    s = sorted(s, key=ord)
    return s[10]
