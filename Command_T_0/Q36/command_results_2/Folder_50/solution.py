def filter_chars(s: str) -> str:
    sliced_s = s[61 + 1:88]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('%' < char < 'q'):
            continue
        result += char

    return result
