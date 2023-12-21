def filter_chars(s: str) -> str:
    sliced_s = s[219 + 1:403]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('*' < char < '7'):
            continue
        result += char

    return result
