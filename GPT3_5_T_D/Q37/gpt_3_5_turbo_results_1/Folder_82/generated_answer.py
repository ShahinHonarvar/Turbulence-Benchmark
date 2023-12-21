
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 12 or i > 25 or char < 'P' or char > 'x':
            filtered_string += char
    return filtered_string
