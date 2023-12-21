def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[521:722 + 1]
    for char in sliced_s:
        if '>' <= char <= '_':
            s = s.replace(char, '')

    return s