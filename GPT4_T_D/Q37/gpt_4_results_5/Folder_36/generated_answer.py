
def filter_chars(s):
    for char in s[259:503]:
        if ',' <= char <= '3':
            s = s.replace(char, '')
    return s
