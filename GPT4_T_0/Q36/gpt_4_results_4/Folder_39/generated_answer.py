
def filter_chars(s):
    for char in s[44:59]:
        if '5' < char < 'C':
            s = s.replace(char, '')
    return s
