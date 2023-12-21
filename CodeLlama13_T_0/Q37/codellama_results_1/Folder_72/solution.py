def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[35:51 + 1]
    for char in sliced_s:
        if 'H' <= char <= 's':
            s = s.replace(char, '')

    return s