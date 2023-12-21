
def remove_repeat_chars(s: str) -> str:
    s1 = s[1:4]
    repeated_chars = [char for char in s1 if s1.count(char) > 1]
    return ''.join(i for i in s if i not in repeated_chars)
