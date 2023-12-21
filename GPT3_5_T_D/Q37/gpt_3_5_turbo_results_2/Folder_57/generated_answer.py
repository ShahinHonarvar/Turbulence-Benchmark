
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 27 <= index <= 85 and '!' <= char <= 'B':
            continue
        filtered_string += char
    return filtered_string
