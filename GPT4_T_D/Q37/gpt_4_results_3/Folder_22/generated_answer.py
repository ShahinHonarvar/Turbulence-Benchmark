
def filter_chars(s):
    for char in s[33:71]:
        if '7' <= char <= 'k':
            s = s.replace(char, '')
    return s
