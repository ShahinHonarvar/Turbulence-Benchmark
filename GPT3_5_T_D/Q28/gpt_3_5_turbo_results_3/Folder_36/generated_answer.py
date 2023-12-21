
def return_nth_smallest_ascii(s):
    substring = s[17:57]
    unique_chars = sorted(set(substring))
    return unique_chars[8]
