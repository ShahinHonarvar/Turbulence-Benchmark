
def filter_chars(s):
    for char in s[36:60]:
        if '!' < char < 'B':
            s = s.replace(char, '')
    return s
