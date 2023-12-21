def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[12:88 + 1]
    for char in sliced_s:
        if '&' <= char <= 'v':
            s = s.replace(char, '')

    return s