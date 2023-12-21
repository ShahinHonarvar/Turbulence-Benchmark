
def return_nth_smallest_ascii(s):
    s = s[5:90]
    s = sorted(s, key=lambda x: ord(x))
    return s[12]
