
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 35 <= i <= 98 and 'A' <= char <= 'b':
            continue
        filtered_string += char
    return filtered_string
