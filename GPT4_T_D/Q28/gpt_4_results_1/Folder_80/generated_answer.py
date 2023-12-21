
def return_nth_smallest_ascii(s):
    valid_chars = s[51:90]
    sorted_chars = sorted(valid_chars, key=ord)
    return sorted_chars[13]
