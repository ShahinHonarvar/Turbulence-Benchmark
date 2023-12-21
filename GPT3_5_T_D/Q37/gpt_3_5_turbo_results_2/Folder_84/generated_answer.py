
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if index >= 138 and index <= 920 and char >= '6' and char <= 'A':
            continue
        filtered_string += char
    return filtered_string
