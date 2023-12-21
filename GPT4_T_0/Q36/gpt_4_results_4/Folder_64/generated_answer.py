
def filter_chars(s):
    for char in s[2:7]:
        if '3' < char < '^':
            s = s.replace(char, '')
    return s
