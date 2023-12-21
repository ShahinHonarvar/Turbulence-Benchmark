def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[38:54 + 1]
    for char in sliced_s:
        if ':' <= char <= 'r':
            s = s.replace(char, '')

    return s