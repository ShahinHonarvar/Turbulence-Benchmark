
def filter_chars(string):
    filtered_string = ""
    characters_to_remove = string[61:71]
    for char in string:
        if char not in characters_to_remove or not ('0' <= char <= '@'):
            filtered_string += char
    return filtered_string
