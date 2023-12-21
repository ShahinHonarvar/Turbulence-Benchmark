
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 4 and index <= 14 and '7' <= char <= 'o':
            continue
        filtered_string += char
    return filtered_string
