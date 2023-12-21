
def return_nth_smallest_ascii(s):
    s = s[4:34]
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[3]
