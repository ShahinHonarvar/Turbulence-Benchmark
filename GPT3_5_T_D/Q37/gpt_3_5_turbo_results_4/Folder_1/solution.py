def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[41:79 + 1]
    for char in sliced_s:
        if 'f' <= char <= '|':
            s = s.replace(char, '')

    return s