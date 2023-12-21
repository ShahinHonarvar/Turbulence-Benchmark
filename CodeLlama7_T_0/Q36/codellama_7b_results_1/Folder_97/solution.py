def filter_chars(s: str) -> str:
    sliced_s = s[309 + 1:591]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('S' < char < 'm'):
            continue
        result += char

    return result
