def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[73:74 + 1]
    for char in sliced_s:
        if 'U' <= char <= 'l':
            s = s.replace(char, '')

    return s