
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 31 <= i <= 38 and ';' <= char <= 'g':
            continue
        filtered_string += char
    return filtered_string
