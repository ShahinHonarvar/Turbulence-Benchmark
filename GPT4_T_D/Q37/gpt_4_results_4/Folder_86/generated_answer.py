
def filter_chars(s):
    for i in range(164, min(707, len(s))):
        if 'O' <= s[i] <= '}':
            s = s.replace(s[i], '')
    return s
