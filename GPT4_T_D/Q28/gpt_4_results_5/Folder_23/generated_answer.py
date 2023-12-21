
def return_nth_smallest_ascii(s):
    chars = sorted(s[29:48])
    return sorted(chars, key = ord)[6]
