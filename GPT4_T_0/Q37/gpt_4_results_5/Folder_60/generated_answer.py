
def filter_chars(s):
    for char in s[12:78]:
        if ':' <= char <= 'L':
            s = s.replace(char, '')
    return s
