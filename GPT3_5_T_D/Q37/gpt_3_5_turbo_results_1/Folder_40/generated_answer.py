
def filter_chars(string):
    first_chars = string[:2]
    filtered_string = ""
    for char in string:
        if char not in first_chars or not ('*' <= char <= 's'):
            filtered_string += char
    return filtered_string
