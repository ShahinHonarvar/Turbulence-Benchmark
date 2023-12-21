
def filter_chars(s):
    substring = s[227:236]
    for char in substring:
        if 'D' <= char <= 'u':
            s = s.replace(char, '')
    return s
