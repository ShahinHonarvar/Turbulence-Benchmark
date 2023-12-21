def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[10:69 + 1]
    for char in sliced_s:
        if 'I' <= char <= 'K':
            s = s.replace(char, '')

    return s