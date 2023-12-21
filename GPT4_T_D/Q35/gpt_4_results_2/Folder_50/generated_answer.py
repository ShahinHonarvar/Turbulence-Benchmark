
def remove_repeat_chars(string):
    range_str = string[14:76]
    chars_to_remove = [char for char in set(range_str) if range_str.count(char) > 1]
    return ''.join(char for char in string if char not in chars_to_remove)
