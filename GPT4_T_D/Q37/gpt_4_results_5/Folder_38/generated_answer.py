
def filter_chars(string):
    filter_range = string[24:80]
    chars_to_remove = [char for char in filter_range if 'a' <= char <= 'f']
    new_string = ''
    for char in string:
        if char not in chars_to_remove:
            new_string += char
    return new_string
