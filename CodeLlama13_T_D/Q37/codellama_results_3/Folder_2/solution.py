def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[477:984 + 1]
    for char in sliced_s:
        if ',' <= char <= 'V':
            s = s.replace(char, '')

    return s