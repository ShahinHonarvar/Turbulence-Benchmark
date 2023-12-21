
def return_nth_smallest_ascii(s):
    substring = s[12:88]
    ascii_values = sorted(ord(c) for c in substring)
    return chr(ascii_values[16])
