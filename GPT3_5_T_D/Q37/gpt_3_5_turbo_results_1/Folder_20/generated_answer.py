
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 25 <= index <= 97 and 'm' <= char <= 'w':
            continue
        filtered_string += char
    return filtered_string
