
def filter_chars(s):
    temp = s[477:948]
    for char in temp:
        if 'b' < char < 'd':
            s = s.replace(char, '')
    return s
