def filter_chars(s: str) -> str:
    sliced_s = s[31 + 1:73]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('M' < char < 'j'):
            continue
        result += char

    return result
