def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[36:40 + 1]
    for char in sliced_s:
        if 'H' <= char <= 'e':
            s = s.replace(char, '')

    return s