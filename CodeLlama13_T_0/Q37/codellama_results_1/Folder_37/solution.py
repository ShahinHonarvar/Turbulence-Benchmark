def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[17:63 + 1]
    for char in sliced_s:
        if 'O' <= char <= '^':
            s = s.replace(char, '')

    return s