
def return_nth_smallest_ascii(s):
    chars = sorted(list(s[12:73]))
    return sorted([ord(ch) for ch in chars])[12]
