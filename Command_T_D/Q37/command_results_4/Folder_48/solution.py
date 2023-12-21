def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[513:877 + 1]
    for char in sliced_s:
        if '?' <= char <= 'n':
            s = s.replace(char, '')

    return s