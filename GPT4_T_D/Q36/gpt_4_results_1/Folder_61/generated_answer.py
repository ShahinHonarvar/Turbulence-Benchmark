
def filter_chars(s):
    for char in s[4:9]:
        if '*' < char < 'E':
            s = s.replace(char, '')
    return s
