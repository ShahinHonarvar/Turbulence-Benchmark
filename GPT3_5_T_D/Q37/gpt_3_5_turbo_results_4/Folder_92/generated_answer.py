
def filter_chars(string):
    chars_to_remove = ''.join(char for char in string[4:5] if '7' <= char <= 'o')
    return string.replace(chars_to_remove, '')
