def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[54:62 + 1]
    for char in sliced_s:
        if ')' <= char <= '9':
            s = s.replace(char, '')

    return s