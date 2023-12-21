
def filter_chars(s):
    for char in s[20:69]:
        if '>' < char < 'C':
            s = s.replace(char, '')
    return s
