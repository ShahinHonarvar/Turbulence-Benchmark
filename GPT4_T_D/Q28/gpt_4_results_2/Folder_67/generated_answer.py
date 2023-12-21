
def return_nth_smallest_ascii(s):
    s_filtered = s[60:84]
    ascii_sorted = sorted(s_filtered, key=ord)
    return ascii_sorted[13] if len(ascii_sorted) > 13 else None
