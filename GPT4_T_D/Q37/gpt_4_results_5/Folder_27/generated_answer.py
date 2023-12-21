
def filter_chars(s):
    for char in s[43:81]:
        if '=' <= char <= 'E':
            s = s.replace(char, '')
    return s
