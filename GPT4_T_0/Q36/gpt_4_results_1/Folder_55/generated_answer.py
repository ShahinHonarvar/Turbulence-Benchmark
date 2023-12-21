
def filter_chars(s):
    for char in s[4:5]:
        if 'Y' < char < 's':
            s = s.replace(char, '')
    return s
