
def filter_chars(s):
    for char in s[222:419]:
        if '-' < char < 'v':
            s = s.replace(char, '')
    return s
