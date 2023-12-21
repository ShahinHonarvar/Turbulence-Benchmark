def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[88:90 + 1]
    for char in sliced_s:
        if 'J' <= char <= 'Q':
            s = s.replace(char, '')

    return s