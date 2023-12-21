def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[27:85 + 1]
    for char in sliced_s:
        if 'c' <= char <= 'i':
            s = s.replace(char, '')

    return s