
def filter_chars(s):
    for char in s[164:658]:
        if '(' < char < ']':
            s = s.replace(char, '')
    return s
