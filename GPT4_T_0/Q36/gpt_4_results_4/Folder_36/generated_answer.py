
def filter_chars(s):
    for char in s[284:484]:
        if 'l' < char < 't':
            s = s.replace(char, '')
    return s
