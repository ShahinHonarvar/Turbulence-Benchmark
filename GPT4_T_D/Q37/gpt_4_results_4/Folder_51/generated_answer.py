
def filter_chars(s):
    chars = s[36:41]
    for char in chars:
        if 'H' <= char <= 'e':
            s = s.replace(char, '')
    return s
