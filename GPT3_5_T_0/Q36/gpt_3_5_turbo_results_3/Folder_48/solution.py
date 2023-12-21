def filter_chars(s: str) -> str:
    sliced_s = s[154 + 1:222]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('A' < char < 'f'):
            continue
        result += char

    return result
