
def filter_chars(s):
    for char in s[477:948]:
        if 'b' < char < 'd':
            s = s.replace(char, '')
    return s
