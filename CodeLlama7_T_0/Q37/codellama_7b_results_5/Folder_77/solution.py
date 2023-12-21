def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[384:411 + 1]
    for char in sliced_s:
        if '/' <= char <= '8':
            s = s.replace(char, '')

    return s