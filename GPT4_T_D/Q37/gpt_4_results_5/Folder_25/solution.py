def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[31:38 + 1]
    for char in sliced_s:
        if ';' <= char <= 'g':
            s = s.replace(char, '')

    return s