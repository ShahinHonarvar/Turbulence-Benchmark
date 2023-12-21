
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 46 <= index <= 85 and '-' <= char <= 'X':
            continue
        filtered_string += char
    return filtered_string
