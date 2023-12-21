
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 18 <= index < 64 and '3' < char < 'B':
            continue
        filtered_string += char
    return filtered_string
