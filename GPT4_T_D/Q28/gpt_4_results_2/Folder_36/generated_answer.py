
def return_nth_smallest_ascii(s):
    substr = s[17:57]
    sorted_chars = sorted(substr, key=ord)
    return sorted_chars[8]
