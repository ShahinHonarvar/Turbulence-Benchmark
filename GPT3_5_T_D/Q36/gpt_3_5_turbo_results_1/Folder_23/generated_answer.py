
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 21 <= index < 25 and '5' < char < '}':
            continue
        filtered_string += char
    return filtered_string
