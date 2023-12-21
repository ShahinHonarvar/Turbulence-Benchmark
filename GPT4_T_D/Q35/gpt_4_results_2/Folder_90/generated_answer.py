
def remove_repeat_chars(s):
    substr = s[307:807]
    chars_to_remove = {ch for ch in substr if substr.count(ch) > 1}
    return ''.join(ch for ch in s if ch not in chars_to_remove)
