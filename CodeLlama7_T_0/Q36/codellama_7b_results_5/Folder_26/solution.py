def filter_chars(s: str) -> str:
    sliced_s = s[43 + 1:83]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and (':' < char < 'Q'):
            continue
        result += char

    return result
