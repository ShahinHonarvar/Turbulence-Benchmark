def filter_chars(s: str) -> str:
    sliced_s = s[669 + 1:888]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('B' < char < 'Y'):
            continue
        result += char

    return result
