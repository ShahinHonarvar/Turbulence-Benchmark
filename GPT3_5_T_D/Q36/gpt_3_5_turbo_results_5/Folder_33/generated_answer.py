
def filter_chars(string):
    to_remove = set(string[299:418])
    filtered_string = ''
    for char in string:
        if char not in to_remove or not ('9' < char < 'P'):
            filtered_string += char
    return filtered_string
