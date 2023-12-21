
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 43 <= index < 59:
            if '5' < char < 'C':
                continue
        filtered_string += char
    return filtered_string
