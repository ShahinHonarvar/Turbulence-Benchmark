
def filter_chars(s):
    for char in s[33:61]:
        if '3' < char < 'D':
            s = s.replace(char, '')
    return s
