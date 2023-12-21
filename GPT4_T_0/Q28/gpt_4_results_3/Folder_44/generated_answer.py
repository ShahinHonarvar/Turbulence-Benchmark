
def return_nth_smallest_ascii(s):
    s = s[20:31]
    sorted_s = sorted(s, key=ord)
    return sorted_s[7]
