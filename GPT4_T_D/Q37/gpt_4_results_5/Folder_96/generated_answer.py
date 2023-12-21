
def filter_chars(s):
    filtered_chars = s[86:93]
    for char in filtered_chars:
        if '!' <= char <= 's':
            s = s.replace(char, '')
    return s
