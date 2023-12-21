
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i < 44 or i >= 48 or not ('+' < char < 'l'):
            filtered_string += char
    return filtered_string
