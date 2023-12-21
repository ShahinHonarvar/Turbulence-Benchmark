
def filter_chars(s):
    return s[:42] + ''.join(c for c in s[42:78] if not ('!' < c < '?')) + s[78:]
