
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 50 <= i < 92 and 'A' < char < 'Q':
            continue
        filtered_string += char
    return filtered_string
