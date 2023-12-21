
def filter_chars(s):
    substring = s[54:84]
    for char in substring:
        if 'j' <= char <= 'v':
            s = s.replace(char, '')
    return s
