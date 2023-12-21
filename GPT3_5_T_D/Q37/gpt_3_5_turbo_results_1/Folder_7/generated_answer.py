
def filter_chars(string):
    filtered_string = ''
    for index, char in enumerate(string):
        if 521 <= index <= 722 and '>' <= char <= '_':
            continue
        filtered_string += char
    return filtered_string
