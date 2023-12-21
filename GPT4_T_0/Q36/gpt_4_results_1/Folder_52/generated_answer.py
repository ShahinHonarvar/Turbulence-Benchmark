
def filter_chars(s):
    for char in s[50:56]:
        if 'I' < char < 'a':
            s = s.replace(char, '')
    return s
