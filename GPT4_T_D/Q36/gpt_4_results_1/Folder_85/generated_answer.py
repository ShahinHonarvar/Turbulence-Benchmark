
def filter_chars(s):
    slice = s[56:80]
    for char in slice:
        if 'S' < char < 's':
            s = s.replace(char, '')
    return s
