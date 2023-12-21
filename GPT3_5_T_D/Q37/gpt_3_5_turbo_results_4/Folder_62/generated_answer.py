
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 10 <= index <= 69 and 'I' <= char <= 'K':
            continue
        filtered_string += char
    return filtered_string
