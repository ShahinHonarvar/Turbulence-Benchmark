def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[26:64 + 1]
    for char in sliced_s:
        if 'V' <= char <= 'o':
            s = s.replace(char, '')

    return s