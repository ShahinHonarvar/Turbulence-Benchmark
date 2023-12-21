def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[46:85 + 1]
    for char in sliced_s:
        if '-' <= char <= 'X':
            s = s.replace(char, '')

    return s