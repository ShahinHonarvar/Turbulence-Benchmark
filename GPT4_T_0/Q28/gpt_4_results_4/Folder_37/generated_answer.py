
def return_nth_smallest_ascii(s):
    s = s[28:68]
    sorted_s = sorted(s, key=ord)
    return sorted_s[14]
