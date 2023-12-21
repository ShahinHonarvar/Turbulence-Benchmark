
def filter_chars(s):
    for char in s[25:37]:
        if 'A' < char < 'h':
            s = s.replace(char, '')
    return s
