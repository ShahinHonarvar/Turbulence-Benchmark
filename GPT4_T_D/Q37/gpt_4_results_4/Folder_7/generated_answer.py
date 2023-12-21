
def filter_chars(s):
    subset = set(s[521:723])
    for char in subset:
        if '>' <= char <= '_':
            s = s.replace(char, '')
    return s
