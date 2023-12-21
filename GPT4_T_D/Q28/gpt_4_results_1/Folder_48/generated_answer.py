
def return_nth_smallest_ascii(s):
    s = s[37:60]
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[5]
