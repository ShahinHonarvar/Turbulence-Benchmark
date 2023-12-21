
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 2 <= index < 7 and 'h' < char < 'k':
            continue
        filtered_string += char
    return filtered_string
