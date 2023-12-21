
def filter_chars(s):
    for char in s[54:63]:
        if ')' <= char <= '9':
            s = s.replace(char, '')
    return s
