def filter_chars(s: str) -> str:
    sliced_s = s[299 + 1:418]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('9' < char < 'P'):
            continue
        result += char

    return result
