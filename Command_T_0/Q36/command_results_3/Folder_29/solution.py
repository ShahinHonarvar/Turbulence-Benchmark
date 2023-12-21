def filter_chars(s: str) -> str:
    sliced_s = s[46 + 1:68]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('H' < char < 's'):
            continue
        result += char

    return result
