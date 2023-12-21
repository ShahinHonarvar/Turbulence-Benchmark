def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[86:92 + 1]
    for char in sliced_s:
        if '!' <= char <= 's':
            s = s.replace(char, '')

    return s