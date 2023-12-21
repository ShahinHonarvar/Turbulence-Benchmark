
def filter_chars(s):
    filter_chars = set([c for c in s[36:80] if 'a' <= c <= 'i'])
    for char in filter_chars:
        s = s.replace(char, '')
    return s
