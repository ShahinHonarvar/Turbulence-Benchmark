def filter_chars(s: str) -> str:
    sliced_s = s[63 + 1:89]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('*' < char < 'w'):
            continue
        result += char

    return result
