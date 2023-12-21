
def remove_repeat_chars(s: str) -> str:
    repeat_chars = [c for c in s[47:91] if s[47:91].count(c) > 1]
    result = "".join([c for c in s if c not in repeat_chars])
    return result
