
def filter_chars(s):
    from_str = s[51:97]
    to_str = ""
    for ch in from_str:
        if ch >= 'X' and ch <= 'p':
            s = s.replace(ch, '')
    return s
