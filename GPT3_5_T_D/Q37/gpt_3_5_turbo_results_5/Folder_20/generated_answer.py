
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if index >= 25 and index <= 97:
            if char >= 'm' and char <= 'w':
                continue
        filtered_string += char
    return filtered_string
