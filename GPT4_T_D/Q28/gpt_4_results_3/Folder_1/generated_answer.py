
def return_nth_smallest_ascii(s):
    s = s[21:60]
    ascii_sorted_chars = sorted(s, key=ord)
    return ascii_sorted_chars[10]
