def filter_chars(s: str) -> str:
    sliced_s = s[323 + 1:526]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and (')' < char < 'O'):
            continue
        result += char

    return result
