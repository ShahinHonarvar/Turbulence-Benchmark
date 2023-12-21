def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[1:5 + 1]
    for char in sliced_s:
        if '$' <= char <= ';':
            s = s.replace(char, '')

    return s