def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[35:40 + 1]
    for char in sliced_s:
        if ')' <= char <= 'l':
            s = s.replace(char, '')

    return s