def filter_chars(s: str) -> str:
    sliced_s = s[18 + 1:31]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('H' < char < '|'):
            continue
        result += char

    return result
