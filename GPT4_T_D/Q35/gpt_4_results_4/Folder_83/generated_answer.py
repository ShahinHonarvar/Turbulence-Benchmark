
def remove_repeat_chars(string):
    chars_in_range = string[101:200]
    chars_to_remove = [char for char in set(chars_in_range) if chars_in_range.count(char) > 1]

    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
