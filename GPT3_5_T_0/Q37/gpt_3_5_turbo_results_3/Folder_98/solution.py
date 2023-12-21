def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[8:9 + 1]
    for char in sliced_s:
        if 'R' <= char <= 't':
            s = s.replace(char, '')

    return s