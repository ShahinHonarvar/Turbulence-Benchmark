
def filter_chars(s):
    for char in s[32:50]:
        if '/' < char < 'J':
            s = s.replace(char, '')
    return s
