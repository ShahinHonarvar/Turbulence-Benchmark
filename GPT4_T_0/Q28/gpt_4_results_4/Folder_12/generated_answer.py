
def return_nth_smallest_ascii(s):
    s = s[3:27]
    s = sorted(s, key=ord)
    return s[4]
