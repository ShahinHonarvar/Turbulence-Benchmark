def filter_chars(s: str) -> str:
    sliced_s = s[27 + 1:75]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('A' < char < 'i'):
            continue
        result += char

    return result
