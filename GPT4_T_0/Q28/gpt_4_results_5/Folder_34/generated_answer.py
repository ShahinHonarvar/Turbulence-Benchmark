
def return_nth_smallest_ascii(s):
    s = s[:19]
    s = sorted(s, key=ord)
    return s[18]
