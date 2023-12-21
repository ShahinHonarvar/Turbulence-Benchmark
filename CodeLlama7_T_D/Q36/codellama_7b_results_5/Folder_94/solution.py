def filter_chars(s: str) -> str:
    sliced_s = s[15 + 1:85]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('I' < char < 'M'):
            continue
        result += char

    return result
