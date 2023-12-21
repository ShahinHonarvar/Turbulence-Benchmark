
def filter_chars(s):
    substr = s[5:8]
    for char in substr:
        if '1' < char < 'J':
            s = s.replace(char, '')
    return s
