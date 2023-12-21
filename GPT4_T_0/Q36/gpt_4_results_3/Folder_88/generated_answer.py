
def filter_chars(s):
    for char in s[79:80]:
        if 'S' < char < '[':
            s = s.replace(char, '')
    return s
