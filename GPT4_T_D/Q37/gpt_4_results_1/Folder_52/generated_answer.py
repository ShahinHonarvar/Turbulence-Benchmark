
def filter_chars(s):
    for char in s[54:84]:
        if 'j' <= char <= 'v':
            s = s.replace(char, '')
    return s
