
def filter_chars(s):
    for char in s[40:87]:
        if '!' < char < '}':
            s = s.replace(char, '')
    return s
