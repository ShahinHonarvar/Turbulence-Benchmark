
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 309 <= i < 591 and 'S' < char < 'm':
            continue
        filtered_string += char
    return filtered_string
