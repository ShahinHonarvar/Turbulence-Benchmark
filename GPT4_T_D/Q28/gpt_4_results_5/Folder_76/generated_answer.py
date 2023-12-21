
def return_nth_smallest_ascii(s):
    s_sub = s[18:67]
    s_sorted = sorted(s_sub, key=lambda x: ord(x))
    return s_sorted[18]
