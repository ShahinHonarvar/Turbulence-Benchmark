def filter_chars(s: str) -> str:
    sliced_s = s[45 + 1:57]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('F' < char < 'n'):
            continue
        result += char

    return result
