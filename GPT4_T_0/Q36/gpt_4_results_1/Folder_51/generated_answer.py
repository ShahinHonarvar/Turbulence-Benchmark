
def filter_chars(s):
    for char in s[59:81]:
        if '5' < char < '>':
            s = s.replace(char, '')
    return s
