
def remove_repeat_chars(s):
    chars_to_remove = [char for char in s[1:3] if s[1:3].count(char) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
