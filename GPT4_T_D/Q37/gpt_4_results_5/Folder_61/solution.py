def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[5:6 + 1]
    for char in sliced_s:
        if 'G' <= char <= 'p':
            s = s.replace(char, '')

    return s