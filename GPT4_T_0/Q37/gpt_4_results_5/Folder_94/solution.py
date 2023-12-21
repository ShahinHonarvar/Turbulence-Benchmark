def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[51:96 + 1]
    for char in sliced_s:
        if 'X' <= char <= 'p':
            s = s.replace(char, '')

    return s