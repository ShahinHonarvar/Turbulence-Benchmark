
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 24 <= i < 37 and 'A' < char < 'h':
            continue
        filtered_string += char
    return filtered_string
