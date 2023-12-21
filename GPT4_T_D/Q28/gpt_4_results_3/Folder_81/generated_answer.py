
def return_nth_smallest_ascii(s):
    limited_string = s[0:14]
    ordered_chars = sorted(limited_string, key=lambda char: ord(char))
    return ordered_chars[13]
