def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[373:901 + 1]
    for char in sliced_s:
        if 'T' <= char <= 'h':
            s = s.replace(char, '')

    return s