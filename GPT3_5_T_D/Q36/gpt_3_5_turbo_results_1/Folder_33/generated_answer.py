
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 299 <= index < 418 and '9' < char < 'P':
            continue
        filtered_string += char
    return filtered_string
