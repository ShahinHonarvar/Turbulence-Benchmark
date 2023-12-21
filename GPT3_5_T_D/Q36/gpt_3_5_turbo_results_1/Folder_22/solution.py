def filter_chars(s: str) -> str:
    sliced_s = s[55 + 1:84]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and (';' < char < 'z'):
            continue
        result += char

    return result
