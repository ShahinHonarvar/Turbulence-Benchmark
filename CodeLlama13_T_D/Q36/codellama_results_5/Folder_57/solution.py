def filter_chars(s: str) -> str:
    sliced_s = s[70 + 1:74]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('A' < char < 'U'):
            continue
        result += char

    return result
