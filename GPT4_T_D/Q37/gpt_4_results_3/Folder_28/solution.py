def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[20:79 + 1]
    for char in sliced_s:
        if '!' <= char <= 'T':
            s = s.replace(char, '')

    return s