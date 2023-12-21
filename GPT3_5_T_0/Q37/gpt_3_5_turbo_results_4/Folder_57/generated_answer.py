
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 27 <= i <= 85 and '!' <= char <= 'B':
            continue
        filtered_string += char
    return filtered_string
