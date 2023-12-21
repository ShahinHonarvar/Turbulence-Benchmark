
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 35 and index <= 89 and char >= 'E' and char <= 't':
            continue
        filtered_string += char
    return filtered_string
