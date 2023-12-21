def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[515:538 + 1]
    for char in sliced_s:
        if '+' <= char <= '}':
            s = s.replace(char, '')

    return s