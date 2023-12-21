
def filter_chars(s):
    for char in s[20:80]:
        if '!' <= char <= 'T':
            s = s.replace(char, "")
    return s
