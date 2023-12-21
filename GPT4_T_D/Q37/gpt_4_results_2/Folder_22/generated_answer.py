
def filter_chars(s):
    characters = set(s[33:71])
    for c in characters:
        if '7' <= c <= 'k':
            s = s.replace(c, '')
    return s
