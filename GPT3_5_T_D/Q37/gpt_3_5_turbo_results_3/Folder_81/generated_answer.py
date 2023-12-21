
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 19 <= index <= 92 and '8' <= char <= 'm':
            continue
        filtered_string += char
    return filtered_string
