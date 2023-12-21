def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[29:79 + 1]
    for char in sliced_s:
        if 'K' <= char <= 'z':
            s = s.replace(char, '')

    return s