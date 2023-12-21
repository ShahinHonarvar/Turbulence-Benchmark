
def filter_chars(string):
    chars_to_remove = set(string[61:88]) - set('%q')
    filtered_string = ''
    for char in string:
        if char not in chars_to_remove:
            filtered_string += char
    return filtered_string
