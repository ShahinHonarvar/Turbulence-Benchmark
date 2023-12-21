def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[71:94 + 1]
    for char in sliced_s:
        if 'K' <= char <= 'a':
            s = s.replace(char, '')

    return s