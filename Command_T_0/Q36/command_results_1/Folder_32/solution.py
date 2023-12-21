def filter_chars(s: str) -> str:
    sliced_s = s[40 + 1:63]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('7' < char < 'H'):
            continue
        result += char

    return result
