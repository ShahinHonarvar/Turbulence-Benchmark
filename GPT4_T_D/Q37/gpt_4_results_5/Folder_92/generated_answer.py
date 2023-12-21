
def filter_chars(string):
    chars_to_remove = [char for char in string[4:5] if '7' <= char <= 'o']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
