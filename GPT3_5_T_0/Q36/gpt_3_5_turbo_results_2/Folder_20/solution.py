def filter_chars(s: str) -> str:
    sliced_s = s[13 + 1:40]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and (':' < char < 'C'):
            continue
        result += char

    return result
