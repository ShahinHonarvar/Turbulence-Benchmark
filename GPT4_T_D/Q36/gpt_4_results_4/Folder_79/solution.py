def filter_chars(s: str) -> str:
    sliced_s = s[11 + 1:46]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('!' < char < 'A'):
            continue
        result += char

    return result
