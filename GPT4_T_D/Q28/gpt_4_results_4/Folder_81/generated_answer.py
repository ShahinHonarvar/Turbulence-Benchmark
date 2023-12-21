
def return_nth_smallest_ascii(s):
    s = s[0:14]
    ascii_char_list = sorted([ord(c) for c in s])
    return chr(ascii_char_list[13])
