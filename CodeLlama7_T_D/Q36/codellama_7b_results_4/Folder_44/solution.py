def filter_chars(s: str) -> str:
    sliced_s = s[18 + 1:64]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('3' < char < 'B'):
            continue
        result += char

    return result
