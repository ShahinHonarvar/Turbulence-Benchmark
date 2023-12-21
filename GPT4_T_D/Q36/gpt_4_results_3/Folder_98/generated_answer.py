
def filter_chars(s):
    for ch in s[5:8]:
        if '1' < ch < 'J':
            s = s.replace(ch, '')
    return s
