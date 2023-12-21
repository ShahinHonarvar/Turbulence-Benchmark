def filter_chars(s: str) -> str:
    sliced_s = s[33 + 1:36]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('>' < char < 'A'):
            continue
        result += char

    return result
