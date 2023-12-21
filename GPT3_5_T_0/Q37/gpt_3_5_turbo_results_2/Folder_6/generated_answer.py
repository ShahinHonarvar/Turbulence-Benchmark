
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 13 <= i <= 28 and 'c' <= char <= 'n':
            continue
        filtered_string += char
    return filtered_string
