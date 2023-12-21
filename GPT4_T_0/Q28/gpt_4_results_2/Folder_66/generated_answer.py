
def return_nth_smallest_ascii(s):
    s = s[35:53]
    s = sorted(s, key=ord)
    return s[9]
