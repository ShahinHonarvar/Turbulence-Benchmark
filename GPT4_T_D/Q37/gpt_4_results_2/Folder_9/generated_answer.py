
def filter_chars(s):
    for ch in s[38:100]:
        if 'A' <= ch <= 'Q':
            s = s.replace(ch, '')

    return s
