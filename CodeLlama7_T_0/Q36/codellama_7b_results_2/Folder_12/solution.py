def filter_chars(s: str) -> str:
    sliced_s = s[32 + 1:84]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('m' < char < 'w'):
            continue
        result += char

    return result
