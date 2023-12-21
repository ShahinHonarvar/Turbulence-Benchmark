def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[22:85 + 1]
    for char in sliced_s:
        if '7' <= char <= 'e':
            s = s.replace(char, '')

    return s