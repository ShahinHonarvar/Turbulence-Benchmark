
def return_nth_smallest_ascii(s):
    s = s[34:86]
    s_sorted = sorted(s, key=lambda x: ord(x))
    return s_sorted[19]
