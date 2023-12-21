
def filter_chars(s):
    for ch in s[259:503]:
        if ',' <= ch <= '3':
            s = s.replace(ch, '')
    return s
