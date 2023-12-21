def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[25:97 + 1]
    for char in sliced_s:
        if 'm' <= char <= 'w':
            s = s.replace(char, '')

    return s