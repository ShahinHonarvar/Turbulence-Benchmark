
def return_nth_smallest_ascii(s):
    s = s[18:46]
    s = sorted(s, key=ord)
    return s[6]
