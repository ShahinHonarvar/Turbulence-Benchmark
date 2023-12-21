
def filter_chars(s):
    for char in s[21:44]:
        if '+' <= char <= '8':
            s = s.replace(char, '')
    return s
