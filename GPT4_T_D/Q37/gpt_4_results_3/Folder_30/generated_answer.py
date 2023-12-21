
def filter_chars(s):
    filtered_chars = s[41:65]
    rest = s[:41] + s[65:]
    for char in filtered_chars:
        if 'K' <= char <= ']':
            s = s.replace(char, '')
    return s
