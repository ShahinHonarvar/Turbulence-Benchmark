
def filter_chars(s):
    for char in s[28:75]:
        if 'A' < char < 'i':
            s = s.replace(char, '')
    return s
