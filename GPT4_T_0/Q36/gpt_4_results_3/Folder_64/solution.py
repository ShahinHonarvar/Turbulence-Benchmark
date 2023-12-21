def filter_chars(s: str) -> str:
    sliced_s = s[1 + 1:7]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('3' < char < '^'):
            continue
        result += char

    return result
