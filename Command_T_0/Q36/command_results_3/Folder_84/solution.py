def filter_chars(s: str) -> str:
    sliced_s = s[171 + 1:636]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('c' < char < 's'):
            continue
        result += char

    return result
