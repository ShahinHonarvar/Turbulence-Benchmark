def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[36:79 + 1]
    for char in sliced_s:
        if '2' <= char <= 's':
            s = s.replace(char, '')

    return s