
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i < 31 or i >= 73 or char <= 'M' or char >= 'j':
            filtered_string += char
    return filtered_string
