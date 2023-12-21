
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 318 < i < 337 and 'B' < char < 'z':
            continue
        filtered_string += char
    return filtered_string
