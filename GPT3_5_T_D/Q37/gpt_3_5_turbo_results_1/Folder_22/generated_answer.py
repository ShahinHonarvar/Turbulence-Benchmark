
def filter_chars(string):
    filtered_string = ""
    for char_index, char in enumerate(string):
        if 33 <= char_index <= 70 and '7' <= char <= 'k':
            continue
        filtered_string += char
    return filtered_string
