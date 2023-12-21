def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[41:86 + 1]
    for char in sliced_s:
        if 'S' <= char <= 's':
            s = s.replace(char, '')

    return s