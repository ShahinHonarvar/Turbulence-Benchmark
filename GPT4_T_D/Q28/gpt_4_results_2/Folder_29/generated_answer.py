
def return_nth_smallest_ascii(s):
    s = s[5:11]
    s_sorted = sorted(s, key=lambda x: ord(x))
    return s_sorted[5]
