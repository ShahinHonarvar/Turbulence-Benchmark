def filter_chars(s: str) -> str:
    sliced_s = s[29 + 1:33]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('%' < char < 'a'):
            continue
        result += char

    return result
