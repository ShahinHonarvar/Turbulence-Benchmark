
def remove_repeat_chars(s):
    chars_7_9 = s[8:9]
    repeat_chars = [char for char in chars_7_9 if chars_7_9.count(char) > 1]
    s = ''.join(char for char in s if char not in repeat_chars)
    return s
