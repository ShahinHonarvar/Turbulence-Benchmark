def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[63:84 + 1]
    for char in sliced_s:
        if 'E' <= char <= '~':
            s = s.replace(char, '')

    return s