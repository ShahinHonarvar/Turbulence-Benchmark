def filter_chars(s: str) -> str:
    sliced_s = s[50 + 1:92]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('A' < char < 'Q'):
            continue
        result += char

    return result
