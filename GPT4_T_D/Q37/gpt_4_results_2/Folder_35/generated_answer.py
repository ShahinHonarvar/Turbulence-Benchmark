
def filter_chars(s):
    filtered_chars = s[155:404]
    for char in filtered_chars:
        if '(' <= char <= ']':
            s = s.replace(char, '')
    return s
