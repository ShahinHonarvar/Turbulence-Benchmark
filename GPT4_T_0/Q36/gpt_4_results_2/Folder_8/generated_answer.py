
def filter_chars(s):
    for char in s[83:93]:
        if '!' < char < '*':
            s = s.replace(char, '')
    return s
