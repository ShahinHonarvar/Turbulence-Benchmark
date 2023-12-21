
def filter_chars(s):
    for c in s[171:195]:
        if '!' < c < '}':
            s = s.replace(c, '')
    return s
