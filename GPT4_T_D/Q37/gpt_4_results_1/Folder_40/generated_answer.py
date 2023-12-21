
def filter_chars(s):
    selected_chars = s[0:2]
    for char in selected_chars:
        if '*' <= char <= 's':
            s = s.replace(char, '')
    return s
