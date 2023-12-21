
def filter_chars(s):
    for char in s[34:36]:
        if '>' < char < 'A':
            s = s.replace(char, '')
    return s
