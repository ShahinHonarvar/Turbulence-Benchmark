
def filter_chars(s):
    for i in s[20:69]:
        if i > '<' and i < 'C':
            s = s.replace(i, '')
    return s
