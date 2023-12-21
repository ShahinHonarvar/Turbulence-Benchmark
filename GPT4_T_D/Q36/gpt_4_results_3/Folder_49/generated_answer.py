
def filter_chars(string):
    chars_to_remove = [char for char in string[47:91] if 'D' < char < 'H']
    for char in chars_to_remove:
        string = string.replace(char, "")
    return string
