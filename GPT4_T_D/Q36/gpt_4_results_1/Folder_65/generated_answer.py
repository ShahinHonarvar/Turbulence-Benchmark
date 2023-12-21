
def filter_chars(s):
    for ch in s[59:82]:
        if ch > 'F' and ch < 'O':
            s = s.replace(ch, '')
    return s
