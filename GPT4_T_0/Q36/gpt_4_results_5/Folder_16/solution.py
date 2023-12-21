def filter_chars(s: str) -> str:
    sliced_s = s[331 + 1:713]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('M' < char < '_'):
            continue
        result += char

    return result
