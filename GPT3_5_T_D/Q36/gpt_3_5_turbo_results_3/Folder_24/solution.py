def filter_chars(s: str) -> str:
    sliced_s = s[10 + 1:15]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('t' < char < 'v'):
            continue
        result += char

    return result
