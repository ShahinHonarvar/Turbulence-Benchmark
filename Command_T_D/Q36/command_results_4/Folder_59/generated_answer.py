def filter_chars(s):
    s = s[:3] + s[8:]
    s = [c for c in s if c in "qwertyuiop"]
    return s
