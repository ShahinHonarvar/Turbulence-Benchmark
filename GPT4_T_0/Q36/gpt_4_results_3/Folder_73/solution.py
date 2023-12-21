def filter_chars(s: str) -> str:
    sliced_s = s[66 + 1:90]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('#' < char < 'T'):
            continue
        result += char

    return result
