
def filter_chars(string):
    chars_to_remove = [char for char in string[384:412] if '/' <= char <= '8']
    for char_to_remove in chars_to_remove:
        string = string.replace(char_to_remove, '')
    return string
