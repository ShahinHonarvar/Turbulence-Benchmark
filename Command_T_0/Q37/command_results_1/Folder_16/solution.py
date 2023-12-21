def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[225:381 + 1]
    for char in sliced_s:
        if 'D' <= char <= 'Y':
            s = s.replace(char, '')

    return s