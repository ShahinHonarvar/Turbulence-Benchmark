def filter_chars(s: str) -> str:
    sliced_s = s[18 + 1:95]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('K' < char < 'a'):
            continue
        result += char

    return result
