def filter_chars(s: str) -> str:
    sliced_s = s[23 + 1:83]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('f' < char < 'o'):
            continue
        result += char

    return result
