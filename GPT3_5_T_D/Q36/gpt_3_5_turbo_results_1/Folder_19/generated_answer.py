
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 77 <= i < 87 and ';' < char < 'r':
            continue
        filtered_string += char
    return filtered_string
