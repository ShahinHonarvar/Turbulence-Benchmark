
def filter_chars(s):
    for char in s[56:84]:
        if ';' < char < 'z':
            s = s.replace(char, "")
    return s
