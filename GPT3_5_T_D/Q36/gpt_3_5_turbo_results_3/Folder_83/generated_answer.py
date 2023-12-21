
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 72 <= index < 93 and '<' < char < 'J':
            continue
        filtered_string += char
    return filtered_string
