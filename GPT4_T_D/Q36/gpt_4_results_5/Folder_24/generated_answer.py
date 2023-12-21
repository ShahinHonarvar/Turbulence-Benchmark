
def filter_chars(s):
    sub_str = s[11:15]
    for char in sub_str:
        if 't' < char < 'v':
            s = s.replace(char, '')
    return s
