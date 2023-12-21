def filter_chars(s: str) -> str:
    sliced_s = s[44 + 1:68]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('W' < char < 'x'):
            continue
        result += char

    return result
