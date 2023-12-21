
def filter_chars(s):
    for char in s[45:68]:
        if 'W' < char < 'x':
            s = s.replace(char, "")
    return s
