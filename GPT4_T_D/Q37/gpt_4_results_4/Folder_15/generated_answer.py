
def filter_chars(s):
    for char in s[2:7]:
        if '?' <= char <= 'f':
            s = s.replace(char, '')
    return s
