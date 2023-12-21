
def filter_chars(s):
    for char in s[15:75]:
        if '9' < char < 'K':
            s = s.replace(char, '')
    return s
