
def filter_chars(s):
    for char in s[70:97]:
        if 'V' < char < 'j':
            s = s.replace(char, '')
    return s
