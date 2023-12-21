def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[20:62 + 1]
    for char in sliced_s:
        if 'i' <= char <= 'k':
            s = s.replace(char, '')

    return s