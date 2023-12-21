
def remove_repeat_chars(s):
    chars_to_remove = {char for char in set(s[45:78]) if s[45:78].count(char) > 1}
    result = "".join(char for char in s if char not in chars_to_remove)
    return result
