def filter_chars(s: str) -> str:
    sliced_s = s[49 + 1:56]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('I' < char < 'a'):
            continue
        result += char

    return result
