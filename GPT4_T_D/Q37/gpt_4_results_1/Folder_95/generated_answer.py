
def filter_chars(s):
    to_be_removed = set([c for c in s[35:41] if ')' <= c <= 'l'])
    for c in to_be_removed:
        s = s.replace(c, "")
    return s
