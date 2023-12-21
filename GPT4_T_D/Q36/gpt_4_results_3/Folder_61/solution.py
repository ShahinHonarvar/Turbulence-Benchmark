def filter_chars(s: str) -> str:
    sliced_s = s[3 + 1:9]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('*' < char < 'E'):
            continue
        result += char

    return result
