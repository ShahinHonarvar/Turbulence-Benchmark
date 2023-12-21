
def filter_chars(s):
    if len(s) > 90:
        for char in set(s[19:91]):
            if 'F' <= char <= 'h':
                s = s.replace(char, '')
    return s
