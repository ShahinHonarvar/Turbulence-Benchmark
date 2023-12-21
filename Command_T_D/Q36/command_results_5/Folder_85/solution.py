def filter_chars(s: str) -> str:
    sliced_s = s[55 + 1:80]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('S' < char < 's'):
            continue
        result += char

    return result
