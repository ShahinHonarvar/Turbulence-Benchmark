
def filter_chars(string):
    chars_to_remove = [char for index, char in enumerate(string) if 12 <= index <= 88 and '&' <= char <= 'v']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
