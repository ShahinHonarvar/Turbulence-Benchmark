
def filter_chars(s):
    for char in s[503:754]:
        if '9' <= char <= 'w':
            s = s.replace(char, '')
    return s
