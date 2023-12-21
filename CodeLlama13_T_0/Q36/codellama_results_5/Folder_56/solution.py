def filter_chars(s: str) -> str:
    sliced_s = s[31 + 1:50]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('/' < char < 'J'):
            continue
        result += char

    return result
