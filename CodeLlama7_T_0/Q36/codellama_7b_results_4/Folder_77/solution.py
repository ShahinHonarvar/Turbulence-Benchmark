def filter_chars(s: str) -> str:
    sliced_s = s[221 + 1:419]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('-' < char < 'v'):
            continue
        result += char

    return result
