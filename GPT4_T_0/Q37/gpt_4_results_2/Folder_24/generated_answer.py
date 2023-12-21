
def filter_chars(s):
    for char in s[36:80]:
        if '2' <= char <= 's':
            s = s.replace(char, '')
    return s
