
def return_nth_smallest_ascii(s):
    s = s[5:11]
    s = sorted(s, key=ord)
    return s[5]
