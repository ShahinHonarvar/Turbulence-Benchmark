
def filter_chars(s):
    for char in s[24:45]:
        if '3' < char < 'I':
            s = s.replace(char, '')
    return s
