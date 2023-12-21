
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if index >= 35 and index <= 51 and 'H' <= char <= 's':
            continue
        filtered_string += char
    return filtered_string
