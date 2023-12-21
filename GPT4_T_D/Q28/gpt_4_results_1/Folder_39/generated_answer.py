
def return_nth_smallest_ascii(s):
    s = s[1:67]
    s = sorted(s, key=lambda x: ord(x))
    return s[7]
