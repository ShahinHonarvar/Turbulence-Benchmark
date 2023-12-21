
def filter_chars(s):
    for char in s[41:63]:
        if '7' < char < 'H':
            s = s.replace(char, '')
    return s
