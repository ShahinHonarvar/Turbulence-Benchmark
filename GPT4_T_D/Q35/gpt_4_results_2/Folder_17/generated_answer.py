
def remove_repeat_chars(s):
    chars_between_index = s[74:84]
    repeat_chars = [char for char in chars_between_index if chars_between_index.count(char) > 1]
    result = ""
    for char in s:
        if char not in repeat_chars:
            result += char
    return result
