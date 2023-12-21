
def filter_chars(s):
    for char in s[12:46]:
        if '!' < char < 'A':
            s = s.replace(char, '')
    return s
