def filter_chars(s: str) -> str:
    sliced_s = s[343 + 1:665]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('%' < char < 'U'):
            continue
        result += char

    return result
