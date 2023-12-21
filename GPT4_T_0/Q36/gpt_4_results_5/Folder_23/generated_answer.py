
def filter_chars(s):
    for char in s[22:25]:
        if '5' < char < '}':
            s = s.replace(char, '')
    return s
