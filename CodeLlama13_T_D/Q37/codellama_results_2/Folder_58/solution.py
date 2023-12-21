def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[503:753 + 1]
    for char in sliced_s:
        if '9' <= char <= 'w':
            s = s.replace(char, '')

    return s