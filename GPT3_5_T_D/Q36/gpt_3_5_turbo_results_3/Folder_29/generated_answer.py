
def filter_chars(string):
    chars_to_remove = set(string[46:68])
    filtered_string = ""
    for char in string:
        if char not in chars_to_remove or char <= 'H' or char >= 's':
            filtered_string += char
    return filtered_string
