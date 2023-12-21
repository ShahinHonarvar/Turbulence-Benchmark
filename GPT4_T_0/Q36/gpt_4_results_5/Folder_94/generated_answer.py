
def filter_chars(s):
    for char in s[16:85]:
        if 'I' < char < 'M':
            s = s.replace(char, '')
    return s
