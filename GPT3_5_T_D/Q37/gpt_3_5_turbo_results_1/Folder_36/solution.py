def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[259:502 + 1]
    for char in sliced_s:
        if ',' <= char <= '3':
            s = s.replace(char, '')

    return s