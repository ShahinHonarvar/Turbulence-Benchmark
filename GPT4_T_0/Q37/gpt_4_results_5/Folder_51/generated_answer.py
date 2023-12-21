
def filter_chars(s):
    for char in s[36:41]:
        if 'H' <= char <= 'e':
            s = s.replace(char, '')
    return s
