
def filter_chars(s):
    for char in s[1:3]:
        if '$' < char < '?':
            s = s.replace(char, '')
    return s
