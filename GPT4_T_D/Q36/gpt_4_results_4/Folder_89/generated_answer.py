
def filter_chars(s):
    for char in s[58:69]:
        if '(' < char < 'W':
            s = s.replace(char, "")
    return s
