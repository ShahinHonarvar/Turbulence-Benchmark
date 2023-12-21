
def filter_chars(s):
    for char in s[19:64]:
        if '3' < char < 'B':
            s = s.replace(char, '')
    return s
