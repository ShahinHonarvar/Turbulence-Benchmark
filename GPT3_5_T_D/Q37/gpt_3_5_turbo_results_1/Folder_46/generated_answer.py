
def filter_chars(string):
    chars_to_remove = [char for char in string[11:73] if 'i' <= char <= 'v']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string
