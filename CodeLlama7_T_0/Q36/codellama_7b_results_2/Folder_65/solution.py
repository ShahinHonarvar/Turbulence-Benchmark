def filter_chars(s: str) -> str:
    sliced_s = s[58 + 1:82]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('F' < char < 'O'):
            continue
        result += char

    return result
