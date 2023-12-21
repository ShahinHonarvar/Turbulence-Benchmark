
def filter_chars(s):
    filtered_chars = s[225:382]
    for char in filtered_chars:
        if 'D' <= char <= 'Y':
            s = s.replace(char, '')
    return s
