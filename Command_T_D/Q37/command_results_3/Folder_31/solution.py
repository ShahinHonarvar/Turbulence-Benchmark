def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[57:96 + 1]
    for char in sliced_s:
        if '<' <= char <= 'w':
            s = s.replace(char, '')

    return s