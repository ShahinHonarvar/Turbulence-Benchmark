
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 27 <= i <= 85 and 'c' <= char <= 'i':
            continue
        filtered_string += char
    return filtered_string
