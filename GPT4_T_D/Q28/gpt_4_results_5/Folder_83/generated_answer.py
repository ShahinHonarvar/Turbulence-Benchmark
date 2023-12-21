
def return_nth_smallest_ascii(s):
    s = s[30:71]
    s = sorted(s, key=lambda x: ord(x))
    return s[14]
