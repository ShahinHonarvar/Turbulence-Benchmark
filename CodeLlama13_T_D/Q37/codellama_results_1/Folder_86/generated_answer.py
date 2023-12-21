
def filter_chars(s):
    for i in range(164, 707):
        if s[i].isalpha() and ord(s[i]) >= ord('O') and ord(s[i]) <= ord('}'):
            s = s.replace(s[i], '')
    return s
