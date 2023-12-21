def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[69:80 + 1]
    for char in sliced_s:
        if '@' <= char <= 'p':
            s = s.replace(char, '')

    return s