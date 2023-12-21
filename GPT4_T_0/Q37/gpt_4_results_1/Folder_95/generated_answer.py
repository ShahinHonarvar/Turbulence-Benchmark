
def filter_chars(s):
    for char in s[35:41]:
        if ')' <= char <= 'l':
            s = s.replace(char, '')
    return s
