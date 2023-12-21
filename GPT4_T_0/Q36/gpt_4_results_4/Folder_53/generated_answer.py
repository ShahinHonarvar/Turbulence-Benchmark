
def filter_chars(s):
    for char in s[91:97]:
        if 'j' < char < 'w':
            s = s.replace(char, '')
    return s
