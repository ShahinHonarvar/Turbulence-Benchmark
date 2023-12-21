
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 19 <= i <= 90 and 'F' <= char <= 'h':
            continue
        filtered_string += char
    return filtered_string
