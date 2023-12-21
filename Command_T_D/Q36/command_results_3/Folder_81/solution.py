def filter_chars(s: str) -> str:
    sliced_s = s[51 + 1:76]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('5' < char < 'f'):
            continue
        result += char

    return result
