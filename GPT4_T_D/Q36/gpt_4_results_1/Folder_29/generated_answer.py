
def filter_chars(string):
    chars_to_remove = [char for char in string[47:68] if 'H' < char < 's']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
