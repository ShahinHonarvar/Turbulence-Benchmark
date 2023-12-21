
def filter_chars(s):
    for char in s[26:65]:
        if 'V' <= char <= 'o':
            s = s.replace(char, "")
    return s
