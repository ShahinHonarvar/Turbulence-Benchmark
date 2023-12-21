
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index in range(43, 81) and '=' <= char <= 'E':
            continue
        filtered_string += char
    return filtered_string
