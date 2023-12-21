
def filter_chars(string):
    char_to_remove = [char for char in string[7:9] if 'B' <= char <= 'H']
    filtered_string = ""
    for char in string:
        if char not in char_to_remove:
            filtered_string += char
    return filtered_string
