def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[124:854 + 1]
    for char in sliced_s:
        if '9' <= char <= 's':
            s = s.replace(char, '')

    return s