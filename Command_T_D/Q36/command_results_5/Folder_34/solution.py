def filter_chars(s: str) -> str:
    sliced_s = s[10 + 1:79]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('?' < char < 'm'):
            continue
        result += char

    return result
