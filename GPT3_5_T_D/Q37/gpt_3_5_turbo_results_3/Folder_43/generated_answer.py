
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 15 <= i <= 55 and 'W' <= char <= '{':
            continue
        filtered_string += char
    return filtered_string
