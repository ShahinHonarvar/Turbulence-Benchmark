def filter_chars(s: str) -> str:
    sliced_s = s[0 + 1:3]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('$' < char < '?'):
            continue
        result += char

    return result
