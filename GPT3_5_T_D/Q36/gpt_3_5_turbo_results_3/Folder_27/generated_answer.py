
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 48 < i < 75:
            if '6' < char < '_':
                continue
        filtered_string += char
    return filtered_string
