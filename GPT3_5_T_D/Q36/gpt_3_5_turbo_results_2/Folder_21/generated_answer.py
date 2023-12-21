
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i < 219 or i >= 403 or char <= '*' or char >= '7':
            filtered_string += char
    return filtered_string
