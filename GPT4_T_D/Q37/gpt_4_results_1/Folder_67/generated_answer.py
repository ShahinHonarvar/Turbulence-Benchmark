
def filter_chars(s):
    filtered_chars = s[19:23]
    for char in filtered_chars:
        if ']' <= char <= 't':
            s = s.replace(char, '')
    return s
