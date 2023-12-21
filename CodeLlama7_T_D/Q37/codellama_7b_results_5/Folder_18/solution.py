def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[770:970 + 1]
    for char in sliced_s:
        if '-' <= char <= 'D':
            s = s.replace(char, '')

    return s