def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[83:99 + 1]
    for char in sliced_s:
        if '*' <= char <= 'j':
            s = s.replace(char, '')

    return s