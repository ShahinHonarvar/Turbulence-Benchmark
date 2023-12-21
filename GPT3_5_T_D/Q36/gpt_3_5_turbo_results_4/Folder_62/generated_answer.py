
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 63 <= i < 89 and '*' < char < 'w':
            continue
        filtered_string += char
    return filtered_string
