
def filter_chars(s):
    characters = set(s[344:665])
    for c in characters:
        if '%' < c < 'U':
            s = s.replace(c, '')
    return s
