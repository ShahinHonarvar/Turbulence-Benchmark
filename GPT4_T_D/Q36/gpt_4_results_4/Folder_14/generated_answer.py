
def filter_chars(s):
    substring = s[42:56]
    for char in substring:
        if 'Z' < char < 'c':
            s = s.replace(char, '')
    return s
