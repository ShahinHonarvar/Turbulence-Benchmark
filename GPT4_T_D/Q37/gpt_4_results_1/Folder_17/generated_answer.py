
def filter_chars(s):
    for char in s[27:30]:
        if ';' <= char <= 'b':
            s = s.replace(char, '')
    return s
