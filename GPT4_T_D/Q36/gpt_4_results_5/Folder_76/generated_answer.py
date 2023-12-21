
def filter_chars(s):
    filter_string = s[670:888]
    for char in set(filter_string):
        if 'B' < char < 'Y':
            s = s.replace(char, '')
    return s
