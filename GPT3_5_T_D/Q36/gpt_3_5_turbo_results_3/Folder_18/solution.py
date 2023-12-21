def filter_chars(s: str) -> str:
    sliced_s = s[587 + 1:648]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and (',' < char < 'c'):
            continue
        result += char

    return result
