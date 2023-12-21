def filter_chars(s: str) -> str:
    sliced_s = s[81 + 1:86]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('!' < char < 's'):
            continue
        result += char

    return result
