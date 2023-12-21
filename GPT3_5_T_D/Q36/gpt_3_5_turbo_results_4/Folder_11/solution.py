def filter_chars(s: str) -> str:
    sliced_s = s[86 + 1:93]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('E' < char < '~'):
            continue
        result += char

    return result
