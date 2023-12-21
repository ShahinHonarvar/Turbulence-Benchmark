
def filter_chars(s):
    chars = set(s[22:25])
    for c in chars:
        if c > '5' and c < '}':
            s = s.replace(c, "")
    return s
