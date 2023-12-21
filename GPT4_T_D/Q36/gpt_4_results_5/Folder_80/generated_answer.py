
def filter_chars(s):
    for char in s[55:92]:
        if  'J' < char < 'X':
            s = s.replace(char, '')
    return s
