
def remove_repeat_chars(s):

    chars_in_range = s[3:5]
    repeat_chars = set([char for char in chars_in_range if chars_in_range.count(char) > 1])

    return "".join([char for char in s if char not in repeat_chars])
