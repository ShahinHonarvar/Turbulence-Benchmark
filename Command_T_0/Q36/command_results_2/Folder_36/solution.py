def filter_chars(s: str) -> str:
    sliced_s = s[283 + 1:484]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('l' < char < 't'):
            continue
        result += char

    return result
