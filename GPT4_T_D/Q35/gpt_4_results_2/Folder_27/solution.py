def remove_repeat_chars(s: str) -> str:
    sliced_s = s[86 + 1:89]
    return ''.join([char for char in s if sliced_s.count(char) <= 1])