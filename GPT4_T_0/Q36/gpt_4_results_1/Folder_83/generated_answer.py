
def filter_chars(s):
    for char in s[73:93]:
        if '>' < char < 'J':
            s = s.replace(char, '')
    return s
