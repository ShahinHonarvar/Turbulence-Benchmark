
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 75 <= index <= 99 and '8' <= char <= 'e':
            continue
        filtered_string += char
    return filtered_string
