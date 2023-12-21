
def return_nth_smallest_ascii(string):
    ascii_chars = list(set(string[29:48]))
    ascii_chars.sort(key=ord)
    return ascii_chars[6] if len(ascii_chars) > 6 else None
