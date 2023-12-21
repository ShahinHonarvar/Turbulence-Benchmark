def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[19:22 + 1]
    for char in sliced_s:
        if ']' <= char <= 't':
            s = s.replace(char, '')

    return s