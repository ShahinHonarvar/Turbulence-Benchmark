
def filter_chars(string):
    filtered_string = ''
    for index, character in enumerate(string):
        if 19 <= index <= 92 and '8' <= character <= 'm':
            continue
        filtered_string += character
    return filtered_string
