
def filter_chars(s):
    for char in s[171:195]:
        if '!' < char < '}':
            s = s.replace(char, '')
    return s
