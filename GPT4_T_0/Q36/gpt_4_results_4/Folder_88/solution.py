def filter_chars(s: str) -> str:
    sliced_s = s[78 + 1:81]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('S' < char < '['):
            continue
        result += char

    return result
