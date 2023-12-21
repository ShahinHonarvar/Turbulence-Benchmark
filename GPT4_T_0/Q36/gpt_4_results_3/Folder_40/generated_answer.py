
def filter_chars(s):
    for char in s[2:7]:
        if '-' < char < 'L':
            s = s.replace(char, '')
    return s
