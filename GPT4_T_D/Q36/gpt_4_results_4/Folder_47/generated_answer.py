
def filter_chars(s):
    for char in s[46:57]:
        if 'F' < char < 'n':
            s = s.replace(char, "")
    return s
