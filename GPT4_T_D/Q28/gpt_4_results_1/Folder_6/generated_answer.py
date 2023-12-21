
def return_nth_smallest_ascii(s):
    s = s[14:55]
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[10]
