
def filter_chars(s):
    substr = s[82:86]
    for char in substr:
        if '!' < char < 's':
            s = s.replace(char, '')
    return s
