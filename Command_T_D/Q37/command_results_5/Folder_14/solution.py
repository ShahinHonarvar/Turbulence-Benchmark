def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[35:98 + 1]
    for char in sliced_s:
        if 'A' <= char <= 'b':
            s = s.replace(char, '')

    return s