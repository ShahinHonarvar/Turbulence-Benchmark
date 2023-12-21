
def filter_chars(s):
    for char in s[24:83]:
        if 'f' < char < 'o':
            s = s.replace(char, '')
    return s
