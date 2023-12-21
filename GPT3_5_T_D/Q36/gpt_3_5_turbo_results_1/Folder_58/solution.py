def filter_chars(s: str) -> str:
    sliced_s = s[318 + 1:337]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('B' < char < 'z'):
            continue
        result += char

    return result
