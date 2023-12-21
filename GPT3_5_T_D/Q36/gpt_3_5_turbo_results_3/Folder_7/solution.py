def filter_chars(s: str) -> str:
    sliced_s = s[502 + 1:946]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('W' < char < 'y'):
            continue
        result += char

    return result
