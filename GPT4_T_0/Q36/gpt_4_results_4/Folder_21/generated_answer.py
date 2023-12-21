
def filter_chars(s):
    for char in s[220:403]:
        if '*' < char < '7':
            s = s.replace(char, '')
    return s
