def filter_chars(s: str) -> str:
    sliced_s = s[4 + 1:8]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('1' < char < 'J'):
            continue
        result += char

    return result
