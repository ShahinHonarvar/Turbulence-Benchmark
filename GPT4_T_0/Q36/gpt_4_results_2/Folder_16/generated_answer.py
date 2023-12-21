
def filter_chars(s):
    for char in s[332:713]:
        if 'M' < char < '_':
            s = s.replace(char, '')
    return s
