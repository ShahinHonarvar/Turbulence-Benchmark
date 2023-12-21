def filter_chars(s: str) -> str:
    sliced_s = s[421 + 1:854]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('D' < char < 'J'):
            continue
        result += char

    return result
