
def filter_chars(s):
    filtered_chars = s[27:86]
    for char in filtered_chars:
        if '!' <= char <= 'B':
            s = s.replace(char, '')
    return s
