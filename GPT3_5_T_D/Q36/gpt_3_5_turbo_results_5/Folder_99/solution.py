def filter_chars(s: str) -> str:
    sliced_s = s[476 + 1:948]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('b' < char < 'd'):
            continue
        result += char

    return result
