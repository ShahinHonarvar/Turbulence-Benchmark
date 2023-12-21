def filter_chars(s: str) -> str:
    sliced_s = s[81 + 1:89]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('f' < char < '{'):
            continue
        result += char

    return result
