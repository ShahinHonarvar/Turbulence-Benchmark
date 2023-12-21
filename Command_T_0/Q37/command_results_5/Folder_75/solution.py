def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[34:67 + 1]
    for char in sliced_s:
        if 'W' <= char <= 'x':
            s = s.replace(char, '')

    return s