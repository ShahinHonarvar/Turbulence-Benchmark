
def return_nth_smallest_ascii(s):
    valid_chars = s[60:89]
    sorted_chars = sorted(valid_chars, key=ord)
    return sorted_chars[6]
