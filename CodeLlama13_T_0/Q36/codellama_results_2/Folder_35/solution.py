def filter_chars(s: str) -> str:
    sliced_s = s[163 + 1:658]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('(' < char < ']'):
            continue
        result += char

    return result
