
def filter_chars(s):
    for char in s[24:83]:
        if '5' <= char <= '<':
            s = s.replace(char, '')
    return s
