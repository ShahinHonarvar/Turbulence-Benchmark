def filter_chars(s: str) -> str:
    if not s:
        return s
    sliced_s = s[348:852 + 1]
    for char in sliced_s:
        if 'J' <= char <= 'b':
            s = s.replace(char, '')

    return s