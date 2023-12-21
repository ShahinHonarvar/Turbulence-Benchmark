
def filter_chars(s):
    for ch in s[35:41]:
        if ')' <= ch <= 'l':
            s = s.replace(ch, '')
    return s
