def filter_chars(s: str) -> str:
    sliced_s = s[42 + 1:78]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('!' < char < '?'):
            continue
        result += char

    return result
