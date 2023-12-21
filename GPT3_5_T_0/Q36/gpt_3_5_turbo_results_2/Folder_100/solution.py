def filter_chars(s: str) -> str:
    sliced_s = s[43 + 1:69]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('B' < char < 'r'):
            continue
        result += char

    return result
