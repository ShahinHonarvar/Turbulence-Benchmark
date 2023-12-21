def filter_chars(s: str) -> str:
    sliced_s = s[90 + 1:97]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('j' < char < 'w'):
            continue
        result += char

    return result
