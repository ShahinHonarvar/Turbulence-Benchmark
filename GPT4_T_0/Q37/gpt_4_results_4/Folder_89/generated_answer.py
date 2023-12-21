
def filter_chars(s):
    for char in s[11:33]:
        if '!' <= char <= '@':
            s = s.replace(char, '')
    return s
