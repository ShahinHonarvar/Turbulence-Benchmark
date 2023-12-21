
def filter_chars(string):
    removed_chars = string[21:25]
    filtered_string = ''
    for char in string:
        if char not in removed_chars:
            filtered_string += char
    return filtered_string
