def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[7:8 + 1]
    for char in sliced_s:
        if 'B' <= char <= 'H':
            s = s.replace(char, '')

    return s