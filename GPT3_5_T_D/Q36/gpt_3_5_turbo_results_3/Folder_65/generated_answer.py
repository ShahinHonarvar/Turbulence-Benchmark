
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 58 <= i < 82 and 'F' < char < 'O':
            continue
        filtered_string += char
    return filtered_string
