
def filter_chars(s):
    for ch in s[24:83]:
        if '5' <= ch <= '<':
            s = s.replace(ch, '')
    return s
