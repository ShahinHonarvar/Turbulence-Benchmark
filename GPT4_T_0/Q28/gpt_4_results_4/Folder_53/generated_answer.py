
def return_nth_smallest_ascii(s):
    s = s[40:61]
    s = sorted(s, key=ord)
    return s[18]
