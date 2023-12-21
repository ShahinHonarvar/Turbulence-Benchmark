def filter_chars(s: str) -> str:
    sliced_s = s[21 + 1:25]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('5' < char < '}'):
            continue
        result += char

    return result
