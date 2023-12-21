
def filter_chars(s):
    for char in s[59:82]:
        if 'F' < char < 'O':
            s = s.replace(char, '')
    return s
