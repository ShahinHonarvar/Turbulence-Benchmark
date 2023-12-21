
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 63 or i >= 89 or (char <= '*' or char >= 'w'):
            filtered_string += char
    return filtered_string
