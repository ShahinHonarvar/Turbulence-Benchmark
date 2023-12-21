def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[51:77 + 1]
    for char in sliced_s:
        if 'V' <= char <= 'Y':
            s = s.replace(char, '')

    return s