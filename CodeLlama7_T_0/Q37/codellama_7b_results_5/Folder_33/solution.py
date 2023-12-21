def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[722:832 + 1]
    for char in sliced_s:
        if 'K' <= char <= 'm':
            s = s.replace(char, '')

    return s