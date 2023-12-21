def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[27:29 + 1]
    for char in sliced_s:
        if ';' <= char <= 'b':
            s = s.replace(char, '')

    return s