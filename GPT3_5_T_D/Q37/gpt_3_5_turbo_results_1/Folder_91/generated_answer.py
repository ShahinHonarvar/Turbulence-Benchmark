
def filter_chars(string):
    char_to_remove = string[7:9]
    filtered_string = ''
    for char in string:
        if char not in char_to_remove or char < 'B' or char > 'H':
            filtered_string += char
    return filtered_string
