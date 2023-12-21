
def return_nth_smallest_ascii(s):
    s = s[34:86]
    sorted_s = sorted(s, key=ord)
    return sorted_s[19]
