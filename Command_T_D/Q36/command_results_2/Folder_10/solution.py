def filter_chars(s: str) -> str:
    sliced_s = s[35 + 1:60]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('!' < char < 'B'):
            continue
        result += char

    return result
