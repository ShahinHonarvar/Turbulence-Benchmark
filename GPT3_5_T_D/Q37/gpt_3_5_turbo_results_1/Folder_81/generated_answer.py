
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 19 <= i <= 92 and '8' <= char <= 'm':
            continue
        filtered_string += char
    return filtered_string
