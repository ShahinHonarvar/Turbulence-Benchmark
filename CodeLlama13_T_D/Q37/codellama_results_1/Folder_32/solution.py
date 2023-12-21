def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[23:89 + 1]
    for char in sliced_s:
        if 'w' <= char <= '{':
            s = s.replace(char, '')

    return s