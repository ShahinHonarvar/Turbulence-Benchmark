
def filter_chars(s):
    for char in s[19:95]:
        if 'K' < char < 'a':
            s = s.replace(char, '')
    return s
