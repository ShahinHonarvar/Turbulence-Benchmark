def filter_chars(s: str) -> str:
    sliced_s = s[31 + 1:70]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('B' < char < 'v'):
            continue
        result += char

    return result
