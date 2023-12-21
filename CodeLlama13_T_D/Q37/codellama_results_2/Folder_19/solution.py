def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[35:89 + 1]
    for char in sliced_s:
        if 'E' <= char <= 't':
            s = s.replace(char, '')

    return s