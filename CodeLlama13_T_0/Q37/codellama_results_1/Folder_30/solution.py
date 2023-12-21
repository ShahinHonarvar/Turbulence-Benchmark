def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[41:64 + 1]
    for char in sliced_s:
        if 'K' <= char <= ']':
            s = s.replace(char, '')

    return s