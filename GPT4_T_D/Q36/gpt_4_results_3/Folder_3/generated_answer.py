
def filter_chars(s):
    for char in s[43:78]:
        if '!' < char < '?':
            s = s.replace(char, '')
    return s
