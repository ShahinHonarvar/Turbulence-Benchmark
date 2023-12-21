def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[52:81 + 1]
    for char in sliced_s:
        if 'A' <= char <= 'U':
            s = s.replace(char, '')

    return s