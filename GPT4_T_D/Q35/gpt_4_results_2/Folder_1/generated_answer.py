
def remove_repeat_chars(s: str) -> str:
    s = list(s)
    sub_string_chars = s[18:88]
    repeat_chars = [char for char in sub_string_chars if sub_string_chars.count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
