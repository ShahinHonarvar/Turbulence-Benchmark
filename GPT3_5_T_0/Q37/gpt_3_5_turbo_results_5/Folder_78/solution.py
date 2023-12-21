def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[75:99 + 1]
    for char in sliced_s:
        if '8' <= char <= 'e':
            s = s.replace(char, '')

    return s