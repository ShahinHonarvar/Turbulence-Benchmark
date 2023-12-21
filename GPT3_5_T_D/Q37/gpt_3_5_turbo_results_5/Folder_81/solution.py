def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[19:92 + 1]
    for char in sliced_s:
        if '8' <= char <= 'm':
            s = s.replace(char, '')

    return s