
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if 33 <= i <= 70 and '7' <= char <= 'k':
            continue
        filtered_string += char
    return filtered_string
