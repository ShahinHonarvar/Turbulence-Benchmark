
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 52 <= i < 88 and '&' < char < 'c':
            continue
        filtered_string += char
    return filtered_string
