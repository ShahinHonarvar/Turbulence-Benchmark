
def filter_chars(s: str) -> str:
    subset = s[29:80]
    for ch in subset:
        if 'K' <= ch <= 'z':
            s = s.replace(ch, '')
    return s
