def filter_chars(s: str) -> str:
    sliced_s = s[1 + 1:6]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and (',' < char < 'f'):
            continue
        result += char

    return result
