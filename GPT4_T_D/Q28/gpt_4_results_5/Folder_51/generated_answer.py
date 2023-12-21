
def return_nth_smallest_ascii(s):
    s = s[10:74]
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[8]
