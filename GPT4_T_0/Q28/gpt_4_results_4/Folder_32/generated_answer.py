
def return_nth_smallest_ascii(s):
    s = s[14:67]
    sorted_s = sorted(s, key=ord)
    return sorted_s[7]
