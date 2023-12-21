def filter_chars(s: str) -> str:
    sliced_s = s[14 + 1:75]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('9' < char < 'K'):
            continue
        result += char

    return result
