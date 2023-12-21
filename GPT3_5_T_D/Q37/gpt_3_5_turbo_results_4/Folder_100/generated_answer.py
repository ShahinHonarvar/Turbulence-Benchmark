
def filter_chars(string):
    chars_to_remove = [char for char in string[88:91] if char >= 'J' and char <= 'Q']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
