
def filter_chars(s):
    for char in s[164:658]:
        if char > '(' and char < ']':
            s = s.replace(char, '')
    return s
