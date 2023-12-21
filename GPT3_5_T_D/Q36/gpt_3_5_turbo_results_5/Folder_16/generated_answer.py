
def filter_chars(string):
    new_string = string[:331] + string[713:]
    filtered_string = ""
    for char in new_string:
        if char <= 'M' or char >= '_':
            filtered_string += char
    return filtered_string
