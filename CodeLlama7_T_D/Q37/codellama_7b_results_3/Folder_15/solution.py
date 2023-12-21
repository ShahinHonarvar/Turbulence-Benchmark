def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[2:6 + 1]
    for char in sliced_s:
        if '?' <= char <= 'f':
            s = s.replace(char, '')

    return s