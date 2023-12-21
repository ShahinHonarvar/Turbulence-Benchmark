
def filter_chars(string):
    chars_to_remove = string[54:63]
    for char in chars_to_remove:
        if ')' <= char <= '9':
            string = string.replace(char, '')
    return string
