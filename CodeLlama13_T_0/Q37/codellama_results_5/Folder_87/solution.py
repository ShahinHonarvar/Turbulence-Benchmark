def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[18:81 + 1]
    for char in sliced_s:
        if 'W' <= char <= '[':
            s = s.replace(char, '')

    return s