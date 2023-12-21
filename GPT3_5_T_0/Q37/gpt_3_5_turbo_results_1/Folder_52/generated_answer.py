
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 54 <= i <= 83 and 'j' <= char <= 'v':
            continue
        filtered_string += char
    return filtered_string
