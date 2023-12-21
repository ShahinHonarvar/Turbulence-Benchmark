def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[10:52 + 1]
    for char in sliced_s:
        if '@' <= char <= 'T':
            s = s.replace(char, '')

    return s