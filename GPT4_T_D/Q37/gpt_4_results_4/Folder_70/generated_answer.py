
def filter_chars(s):
    substring = s[515:539]
    for c in substring:
        if '+' <= c <= '}':
            s = s.replace(c, '')
    return s
