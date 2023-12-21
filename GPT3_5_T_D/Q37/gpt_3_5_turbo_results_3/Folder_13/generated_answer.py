
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 124 <= index <= 854 and '9' <= char <= 's':
            continue
        filtered_string += char
    return filtered_string
