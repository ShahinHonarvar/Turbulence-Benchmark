
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 11 <= index <= 72 and 'i' <= char <= 'v':
            continue
        filtered_string += char
    return filtered_string
