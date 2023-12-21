def filter_chars(s: str) -> str:
    sliced_s = s[24 + 1:37]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('A' < char < 'h'):
            continue
        result += char

    return result
