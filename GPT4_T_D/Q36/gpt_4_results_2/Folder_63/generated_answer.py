
def filter_chars(s):
    characters = set(s[27:80])
    for ch in characters:
        if '<' < ch < '>':
            s = s.replace(ch, '')
    return s
