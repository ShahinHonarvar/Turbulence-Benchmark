def filter_chars(s: str) -> str:
    sliced_s = s[672 + 1:709]
    if not sliced_s:
        return s
    result = ''
    for char in s:
        if char in sliced_s and ('X' < char < '}'):
            continue
        result += char

    return result
