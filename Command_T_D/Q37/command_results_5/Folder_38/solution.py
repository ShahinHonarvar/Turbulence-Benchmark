def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[24:79 + 1]
    for char in sliced_s:
        if 'a' <= char <= 'f':
            s = s.replace(char, '')

    return s