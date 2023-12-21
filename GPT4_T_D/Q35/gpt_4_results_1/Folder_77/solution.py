def remove_repeat_chars(s: str) -> str:
    sliced_s = s[355 + 1:988]
    return ''.join([char for char in s if sliced_s.count(char) <= 1])