
def filter_chars(s):
    sub_string = s[42:93]
    for c in sub_string:
        if '/' <= c <= 'a':
            s = s.replace(c, '')
    return s
