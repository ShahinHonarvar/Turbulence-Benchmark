
def filter_chars(s):
    for char in s[19:34]:
        if 'S' <= char <= '{':
            s = s.replace(char, '')
    return s
