def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[12:77 + 1]
    for char in sliced_s:
        if ':' <= char <= 'L':
            s = s.replace(char, '')

    return s