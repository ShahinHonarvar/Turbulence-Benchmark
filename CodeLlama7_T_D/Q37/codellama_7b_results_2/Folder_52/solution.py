def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[54:83 + 1]
    for char in sliced_s:
        if 'j' <= char <= 'v':
            s = s.replace(char, '')

    return s