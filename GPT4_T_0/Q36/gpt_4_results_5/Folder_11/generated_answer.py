
def filter_chars(s):
    for char in s[87:93]:
        if 'E' < char < '~':
            s = s.replace(char, '')
    return s
