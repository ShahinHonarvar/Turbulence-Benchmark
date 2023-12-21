
def filter_chars(s):
    for char in s[2:9]:
        if '8' < char < 'm':
            s = s.replace(char, '')
    return s
