def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[19:32 + 1]
    for char in sliced_s:
        if 'f' <= char <= 'o':
            s = s.replace(char, '')

    return s