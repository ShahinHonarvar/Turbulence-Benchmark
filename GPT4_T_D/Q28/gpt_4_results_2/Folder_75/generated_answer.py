
def return_nth_smallest_ascii(s):
    s = s[62:84]
    ordered_chars = sorted(s, key=lambda x: ord(x))
    return ordered_chars[8]
