
def filter_chars(s):
    to_remove = []
    if len(s) >= 9:
        for ch in s[7:9]:
            if 'B' <= ch <= 'H':
                to_remove.append(ch)
    for tr in set(to_remove):
        s = s.replace(tr, '')
    return s
