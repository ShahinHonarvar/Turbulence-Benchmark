
def filter_chars(s):
    filter_chars = set([c for c in s[73:75] if 'U' <= c <= 'l'])
    for char in filter_chars:
        s = s.replace(char, '')
    return s
