def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[71:96 + 1]
    for char in sliced_s:
        if '_' <= char <= 'o':
            s = s.replace(char, '')

    return s