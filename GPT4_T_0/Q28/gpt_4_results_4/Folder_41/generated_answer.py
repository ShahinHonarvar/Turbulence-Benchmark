
def return_nth_smallest_ascii(s):
    s = s[58:86]
    sorted_s = sorted(s, key=ord)
    return sorted_s[18]
