def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[32:46 + 1]
    for char in sliced_s:
        if '0' <= char <= 'k':
            s = s.replace(char, '')

    return s