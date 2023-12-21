
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 54 <= index <= 83 and 'j' <= char <= 'v':
            continue
        filtered_string += char
    return filtered_string
