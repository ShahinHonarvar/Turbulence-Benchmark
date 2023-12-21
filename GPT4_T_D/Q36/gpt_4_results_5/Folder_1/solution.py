def filter_chars(s: str) -> str:
    sliced_s = s[69 + 1:87]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('#' < char < 'L'):
            continue
        result += char

    return result
