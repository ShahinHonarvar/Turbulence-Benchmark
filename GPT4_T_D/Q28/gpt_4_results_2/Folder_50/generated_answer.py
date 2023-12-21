
def return_nth_smallest_ascii(s):
    ascii_chars = [c for i, c in enumerate(s) if 25 <= i <= 88]
    ascii_chars.sort(key=ord)
    return ascii_chars[10]
