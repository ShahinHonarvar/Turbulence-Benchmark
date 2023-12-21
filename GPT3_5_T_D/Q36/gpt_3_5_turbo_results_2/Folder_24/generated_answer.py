
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 10 <= i < 15 and 't' < char < 'v':
            continue
        filtered_string += char
    return filtered_string
