
def filter_chars(s):
    filtered_chars = s[2:7]
    for char in set(filtered_chars):
        if '?' <= char <= 'f':
            s = s.replace(char, '')
    return s
