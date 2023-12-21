def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[28:65 + 1]
    for char in sliced_s:
        if 'O' <= char <= 'd':
            s = s.replace(char, '')

    return s